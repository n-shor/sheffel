import os
from llvmlite import ir

from .file_constants import *

from ..ast.nodes import Node
from .translator.function import EntryFunction


def create_ir(ast: list[Node]):
    """Creates an IR file from the AST."""

    module = ir.Module()

    func = EntryFunction(module)

    func.translate(ast)

    # mr = binding.parse_assembly(str(module))

    # print(mr.triple)
    # print(mr.name)
    # print(mr.source_file)

    with open(f'{BUILD_PATH}/{IR_FILE}', 'w') as f:
        f.write(str(module))


if not os.path.isdir(BUILD_PATH):
    os.makedirs(BUILD_PATH)
