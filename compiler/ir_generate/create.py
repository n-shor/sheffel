import os
from llvmlite import ir

from .file_constants import *

from ..ast.nodes import Node
from .translator.function import make_entry_function


def create_ir(statements: list[Node]):
    """Creates an IR file from the AST."""

    module = ir.Module()

    func = make_entry_function(module, statements)

    func.translate()

    # mr = binding.parse_assembly(str(module))

    # print(mr.triple)
    # print(mr.name)
    # print(mr.source_file)

    with open(f'{BUILD_PATH}/{IR_FILE}', 'w') as f:
        f.write(str(module))


if not os.path.isdir(BUILD_PATH):
    os.makedirs(BUILD_PATH)
