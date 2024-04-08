from __future__ import annotations

from llvmlite import ir

from ..structure import abstract
from ..structure import assembly


class ModuleAssembler(assembly.Scope):
    """Translates abstract node representation into a llvm ir module."""
    def __init__(self):
        super().__init__(None)  # no parent
        self.module = ir.Module()

    def translate(self, main: abstract.Node) -> ir.Module:
        main_function_type = ir.FunctionType(ir.IntType(32), ())
        main_function = ir.Function(self.module, main_function_type, 'main')
        assembler = FunctionAssembler(main_function, self)
        assembler.translate(main)
        return self.module


class FunctionAssembler(assembly.Scope):
    """Writes the code for a llvm ir function."""

    def __init__(self, function: ir.Function, parent: assembly.Scope):
        super().__init__(parent)
        self.function = function

    def translate(self, source: abstract.Node):
        block = self.function.append_basic_block()
        assembler = BlockAssembler(ir.IRBuilder(block), self)
        assembler.translate(source)


class BlockAssembler(assembly.Scope):
    """Writes the code for a llvm ir basic block."""

    def __init__(self, builder: ir.IRBuilder, parent: assembly.Scope):
        super().__init__(parent)
        self.builder = builder

    def translate(self, source: abstract.Node):
        pass












