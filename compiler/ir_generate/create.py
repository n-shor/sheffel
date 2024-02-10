from llvmlite import ir

from ..ast.nodes import Block
from .function_translator import make_entry_function


def create_ir(program: Block):
    """Creates an IR module from the AST."""

    module = ir.Module()

    func = make_entry_function(module, program)

    func.translate()

    return module
