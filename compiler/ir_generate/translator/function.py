from llvmlite import ir

from compiler.ast.nodes import *
from ..ir_constants import ENTRY_LABEL_NAME, ENTRY_LABEL_FUNC_TYPE

from .block import Block


class Function:
    def __init__(self, name: str, func_type: ir.FunctionType, module: ir.Module):

        self.module = module
        self.func = ir.Function(self.module, func_type, name)

    def translate(self, code: list[Node]):
        Block(self.func).translate(code)


class EntryFunction(Function):
    def __init__(self, module: ir.Module):
        super().__init__(ENTRY_LABEL_NAME, ENTRY_LABEL_FUNC_TYPE, module)