from enum import Enum, auto

from llvmlite import ir

from ...ast import nodes
from ...ast.nodes import *
from ...ast.types import *

from .type_resolver import resolve as resolve_type
from .scope import Scope


class Block(Scope):
    """A translation unit consisting of many uninterrupted lines."""

    def __init__(self, syntax: nodes.Block, func: ir.Function, parent: Scope):
        self.statements = syntax.statements
        self.func = func
        self.block = self.func.append_basic_block()
        self.builder = ir.IRBuilder(self.block)

        super().__init__(parent, {})

    def add(self, statement: Node, **kwargs) -> ir.Value | ir.Instruction:
        """Adds a statement to the block."""

        match statement:

            case Literal(value=value, type_=LiteralType() as type_):
                return ir.Constant(resolve_type(type_), value)

            case nodes.Block() as syntax:
                next_ = Block(syntax, self.func, self)
                next_.translate()
                return self.builder.branch(next_.block)

            case Return(returnee=returnee):
                return self.builder.ret(self.add(returnee, **kwargs))

            case nodes.Function() as syntax:
                func_builder = function.Function(syntax, self.func.module)
                func_builder.translate()
                return func_builder.func

            case VariableDeclaration(name=name, type_=type_):
                return self.allocate(name, resolve_type(type_), self.builder)

            case Variable(name=name):
                return (self.write if 'write' in kwargs else self.read)(name, self.builder)

            # negative literal
            case Operator(signature='-', operands=(Literal(value=value, type_=NumericLiteralType() as type_),)):
                return ir.Constant(resolve_type(type_), -value)

            case Operator(signature='+', operands=(left, right)):
                return self.builder.add(self.add(left, **kwargs), self.add(right, **kwargs))

            case Operator(signature='-', operands=(left, right)):
                return self.builder.sub(self.add(left, **kwargs), self.add(right, **kwargs))

            case Operator(signature='*', operands=(left, right)):
                return self.builder.mul(self.add(left, **kwargs), self.add(right, **kwargs))

            case Operator(signature='()', operands=(callee, *parameters)):
                return self.builder.call(self.add(callee, **kwargs), (self.add(param, **kwargs) for param in parameters))

            case Operator(signature='=', operands=(assigned, assignee)):
                return self.builder.store(
                    self.add(assignee, **kwargs),
                    self.add(assigned, write=True, **kwargs)
                )

            case Operator(signature=signature):
                raise ValueError(f'{signature} is an unknown operation.')

            case Node():
                raise TypeError(f'{statement} is of a primitive or unknown node type.')

            case _:
                raise TypeError(f'{statement} is not a node type.')

    def translate(self) -> bool:
        """Translates the entire block. Returns whether it is successfully terminated."""

        for statement in self.statements:

            match self.add(statement):
                case ir.Terminator():
                    return True

        return False


from . import function
