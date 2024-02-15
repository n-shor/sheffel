from llvmlite import ir, binding

from ..ast.nodes import Block
from .function_translator import make_entry_function
from . import static


def create_ir(program: Block):
    """Creates an IR module from the AST."""

    module = ir.Module()

    module.triple = binding.get_default_triple()

    static.libc.add_all_to(module)
    static.managed.add_all_to(module)

    func = make_entry_function(module, program)

    func.translate()

    return module
