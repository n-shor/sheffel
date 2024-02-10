from llvmlite import ir, binding

from ..ast.nodes import Block
from .function_translator import make_entry_function


def create_ir(program: Block):
    """Creates an IR module from the AST."""

    module = ir.Module()

    module.triple = binding.get_default_triple()

    ir.Function(module, ir.FunctionType(ir.IntType(8).as_pointer(), (ir.IntType(64), )), 'malloc')
    ir.Function(module, ir.FunctionType(ir.VoidType(), (ir.IntType(8).as_pointer(), )), 'free')

    func = make_entry_function(module, program)

    func.translate()

    return module
