from llvmlite import ir, binding

from ..ast.nodes import Block
from .function_translator import make_entry_function
from . import external


def create_ir(program: Block):
    """Creates an IR module from the AST."""

    module = ir.Module()

    module.triple = binding.get_default_triple()

    external.malloc.add(module)
    external.free.add(module)

    func = make_entry_function(module, program)

    func.translate()

    return module
