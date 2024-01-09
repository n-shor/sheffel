from llvmlite import ir

import compiler.ast.nodes as nodes
from ..ir_constants import ENTRY_LABEL_NAME, ENTRY_LABEL_FUNC_TYPE

from .block import Block
from .type_resolver import resolve as resolve_type


class Function:
    def __init__(self, name: str, syntax: nodes.Function, module: ir.Module):
        self.syntax = syntax
        self.module = module
        self.func = ir.Function(module, resolve_type(syntax.type_), name)

    def translate(self):
        """Translates the function. Returns whether it is successfully terminated."""
        return Block(self.syntax.block, self.func).translate()


class EntryFunction(Function):
    def __init__(self, module: ir.Module):
        super().__init__(ENTRY_LABEL_NAME, ENTRY_LABEL_FUNC_TYPE, module)
    
    def translate(self):
        if not (block := Block(self.syntax.block, self.func)).translate():
            block.builder.ret(self.func.function_type.return_type(0))

        return True
