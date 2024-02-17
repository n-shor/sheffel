from llvmlite import ir, binding

from ..ast.nodes import Block
from .function_translator import make_entry_function
from .lib import managed


def create_ir(program: Block) -> tuple[ir.Module, ...]:
    """Creates an IR module from the AST."""

    module = ir.Module()
    module.triple = binding.get_default_triple()

    managed.module.add_to(module)

    func = make_entry_function(module, program)

    func.translate()

    return module, managed.module.module
