from __future__ import annotations

from llvmlite import ir

from ..structure import resolved

from . import ITranslator


class ModuleAssembler(ITranslator[resolved.Node, ir.Module]):
    """Translates abstract node representation into a llvm ir module."""
    def __init__(self):
        self.module = ir.Module()

    def translate(self, source):
        main_function_type = ir.FunctionType(ir.IntType(32), ())
        main_function = ir.Function(self.module, main_function_type, 'main')
        assembler = FunctionAssembler(main_function)
        assembler.translate(source)
        return self.module


class FunctionAssembler(ITranslator[resolved.Node, None]):
    """Writes the code for a llvm ir function."""

    def __init__(self, empty_function: ir.Function):
        self.function = empty_function

    def translate(self, source):
        block = self.function.append_basic_block()
        assembler = BlockAssembler(ir.IRBuilder(block))
        assembler.translate(source)


class BlockAssembler(ITranslator[resolved.Node, None]):
    """Writes the code for a llvm ir basic block."""

    def __init__(self, builder: ir.IRBuilder):
        self.builder = builder

    def translate(self, source):

        match source:
            case _:
                pass











