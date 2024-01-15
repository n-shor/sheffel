from llvmlite import ir

from ...ast import nodes
from ...ast.nodes import *
from ...ast.types import *

from .type_resolver import resolve as resolve_type
from .variable_scope import VariableScope


class Block(VariableScope):
    """A translation unit consisting of many uninterrupted lines."""

    def __init__(self, syntax: nodes.Block, func: ir.Function, parent: VariableScope):
        self.statements = syntax.statements
        self.func = func
        self.block = self.func.append_basic_block()
        self.builder = ir.IRBuilder(self.block)

        self._binary_operators = {
            '+': self.builder.add,
            '-': self.builder.sub,
            '*': self.builder.mul,
        }

        super().__init__(parent, {})

    def add(self, statement: Node) -> ir.Value | ir.Instruction:
        """Adds a statement to the block."""

        match statement:

            case Literal(value=value, type_=LiteralType() as type_):
                return ir.Constant(resolve_type(type_), value)

            case nodes.Block() as syntax:
                next_ = Block(syntax, self.func, self)
                next_.translate()
                return self.builder.branch(next_.block)

            case Return(returnee=returnee):
                return self.builder.ret(self.add(returnee))

            case nodes.Function() as syntax:
                func_builder = function.Function(syntax, self.func.module)
                func_builder.translate()
                return func_builder.func
                # should allocate a function pointer type

            case VariableDeclaration(name=name, type_=type_):
                return self.add_named_allocation(name, self.builder.alloca(resolve_type(type_)))

            case WriteVariable(name=name):
                return self.get_named_allocation(name)

            case ReadVariable(name=name):
                return self.load_any(name, self.builder)

            # negative literal
            case UnaryOperator(signature='-', operands=(Literal(value=value, type_=NumericLiteralType() as type_), )):
                return ir.Constant(resolve_type(type_), -value)

            case BinaryOperator(signature='=', operands=(assigned, assignee)):
                return self.builder.store(
                    self.add(assignee),
                    self.add(assigned)
                )

            case BinaryOperator(signature=signature, operands=(left, right)) if signature in self._binary_operators:
                return self._binary_operators[signature](self.add(left), self.add(right))

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
