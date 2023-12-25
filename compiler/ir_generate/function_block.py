from __future__ import annotations

from llvmlite import ir

from .ir_constants import *
from ..ast.nodes import *


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

    def translate(self, node: Node):
        match node:
            case IntegralLiteral(value=value):
                return ir.Constant(int32_t, value)

            case VariableDeclaration(name=name, value_type=value_type):
                allocated = self.builder.alloca(value_type)
                self._stack_variables[name] = allocated
                return allocated

            case Variable(name=name):
                return self.builder.load(self._stack_variables[name])

            case BinaryOperator(signature='=', operands=(VariableDeclaration(name=assigned_name, value_type=value_type), assignee)):
                allocated = self.builder.alloca(value_type)
                self._stack_variables[assigned_name] = allocated
                return self.builder.store(self.translate(assignee), allocated)

            case BinaryOperator(signature='=', operands=(Variable(name=assigned_name), assignee)):
                return self.builder.store(
                    self.translate(assignee),
                    self._stack_variables[assigned_name]
                )

            case BinaryOperator(signature='='):
                raise ValueError(f'Cannot assign to a non-variable.')

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