from llvmlite import ir

from .ir_constants import ENTRY_LABEL_NAME, ENTRY_LABEL_FUNC_TYPE
from ..ast.nodes import *
from ..ast.types.literal_type import *


class FunctionBlock:
    def __init__(self, name: str, func_type: ir.FunctionType, module: ir.Module):
        self.module = module

        self.func = ir.Function(self.module, func_type, name)
        self.block = self.func.append_basic_block()
        self.builder = ir.IRBuilder(self.block)

        self._binary_operators = {
            '+': self.builder.add,
            '-': self.builder.sub,
            '*': self.builder.mul,
        }

        self._stack_variables: dict[str, ir.AllocaInstr] = {}

        self._types: dict[str, ir.Type] = {
            'Int': ir.IntType(32),
            'Float': ir.FloatType()
        }

    def translate(self, node: Node):
        match node:
            case Literal(value=value, type_=LiteralType(type_=type_)):
                return ir.Constant(type_, value)

            # negative literals
            case UnaryOperator(signature='-', operands=(Literal(value=value, type_=NumericLiteralType(type_=type_)), )):
                return ir.Constant(type_, -value)

            case VariableDeclaration(name=name, type_=VariableType(base_type=type_, memory=ValueMemoryQualifier())):
                allocated = self.builder.alloca(type_)
                self._stack_variables[name] = allocated
                return allocated

            case WriteVariable(name=name):
                return self._stack_variables[name]

            case ReadVariable(name=name):
                return self.builder.load(self._stack_variables[name])

            case BinaryOperator(signature='=', operands=(assigned, assignee)):
                return self.builder.store(
                    self.translate(assignee),
                    self.translate(assigned)
                )

            case BinaryOperator(signature=signature, operands=(left, right)) if signature in self._binary_operators:
                return self._binary_operators[signature](self.translate(left), self.translate(right))

            case Operator(signature=signature):
                raise ValueError(f'{signature} is an unknown operation.')

            case Node():
                raise TypeError(f'{node} is of a primitive or unknown node type.')

            case _:
                raise TypeError(f'{node} is not a node type.')


class EntryFunctionBlock(FunctionBlock):
    def __init__(self, module: ir.Module):
        super().__init__(ENTRY_LABEL_NAME, ENTRY_LABEL_FUNC_TYPE, module)
