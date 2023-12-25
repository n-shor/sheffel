import os
from llvmlite import ir

from .file_constants import *

from ..ast.nodes import Node
from .function_block import FunctionBlock, EntryFunctionBlock


def create_ir(ast: list[Node]):
    """Creates an IR file from the AST."""

    module = ir.Module()

    func = EntryFunctionBlock(module)

    for node in ast:
        func.translate(node)

    with open(f'{BUILD_PATH}/{IR_FILE}', 'w') as f:
        f.write(str(module))


if not os.path.isdir(BUILD_PATH):
    os.makedirs(BUILD_PATH)
