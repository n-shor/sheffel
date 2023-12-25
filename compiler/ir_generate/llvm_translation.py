from __future__ import annotations

from llvmlite import ir

from .ir_constants import *
from ..ast.nodes import *

int32_type = ir.IntType(32)
basic_func_type = ir.FunctionType(int32_type, ())


def make_exception_raiser(e: Exception):
    def exception_raiser(*args, **kwargs):
        raise e
    return exception_raiser


class Function:
    def __init__(self, module: ir.Module):
        self.module = module

        self.func = ir.Function(self.module, basic_func_type, name=ENTRY_LABEL_NAME)
        self.block = self.func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(self.block)

    def translate(self, node: Node):

        match node:
            case IntegralLiteral(value=value):
                return ir.Constant(int32_type, value)

            case BinaryOperator(signature=signature, operands=(left, right)):
                return {
                    '+': self.builder.add,
                    '-': self.builder.sub,
                    '*': self.builder.mul
                }.get(signature,
                      make_exception_raiser(ValueError(f'{signature} is an unknown operation.'))
                      )(self.translate(left), self.translate(right))

            case Node():
                raise TypeError(f'{node} is of a primitive or unknown node type.')

            case _:
                raise TypeError(f'{node} is not a node type.')

    def translate_lines(self, ast: list[Node]):
        for node in ast:
            self.translate(node)

    def get_ir(self):
        return str(self.module)
