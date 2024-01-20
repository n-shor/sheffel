import os
from llvmlite import ir

from .file_constants import *

from ..ast.nodes import Block
from .translator.function import make_entry_function


def create_ir(program: Block):
    """Creates an IR module from the AST."""

    module = ir.Module()

    func = make_entry_function(module, program)

    func.translate()

    # mr = binding.parse_assembly(str(module))

    # print(mr.triple)
    # print(mr.name)
    # print(mr.source_file)

    return module
