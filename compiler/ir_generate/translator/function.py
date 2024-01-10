from llvmlite import ir

from ...ast import nodes
from ...ast.types import FunctionType, VariableType, IntegralLiteralType, DirectUnqualifiedType, ValueMemoryQualifier
from ..ir_constants import ENTRY_LABEL_NAME

from .block import Block
from .type_resolver import resolve as resolve_type


class Function:
    def __init__(self, name: str, syntax: nodes.Function, module: ir.Module):
        self.body = syntax.body
        self.module = module
        self.func = ir.Function(module, resolve_type(syntax.type_), name)

    def translate(self):
        """Translates the function. Returns whether it is successfully terminated."""
        return Block(self.body, self.func).translate()


def make_entry_function(module: ir.Module, body: nodes.Block):

    return_type = VariableType(DirectUnqualifiedType(ir.IntType(32)), ValueMemoryQualifier())
    func_type = FunctionType(return_type=return_type)
    func = nodes.Function(func_type, body)

    return Function(ENTRY_LABEL_NAME, func, module)
