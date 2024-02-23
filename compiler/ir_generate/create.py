from llvmlite import ir, binding

from ..ast.nodes import Block
from .function_translator import make_entry_function
from .lib import managed, libc


def create_ir(program: Block) -> tuple[ir.Module, ...]:
    """Creates an IR module from the AST."""

    module = ir.Module()
    module.triple = binding.get_default_triple()

    managed.generic.add_to(module)
    libc.utils.add_to(module)

    func = make_entry_function(module, program)

    func.translate()

    return module, managed.generic.module
