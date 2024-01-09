from llvmlite import ir

from ...ast import nodes
from ...ast.types import FunctionType, VariableType, IntegralLiteralType, DirectUnqualifiedType, ValueMemoryQualifier
from ..ir_constants import ENTRY_LABEL_NAME

from .block import Block
from .type_resolver import resolve as resolve_type


class Function:
    def __init__(self, name: str, syntax: nodes.Function, module: ir.Module):
        self.syntax = syntax
        self.module = module
        self.func = ir.Function(module, resolve_type(syntax.type_), name)

    def translate(self):
        """Translates the function. Returns whether it is successfully terminated."""
        return Block(self.syntax.block, self.func).translate()


def make_entry_function(module: ir.Module, statements: list[nodes.Node]):

    return_type = VariableType(DirectUnqualifiedType(ir.IntType(32)), ValueMemoryQualifier())
    func_type = FunctionType(return_type=return_type)

    return_statement = nodes.Return(nodes.Literal(0, IntegralLiteralType()))
    func_body = nodes.Block(*statements, return_statement)

    return Function(ENTRY_LABEL_NAME, nodes.Function(func_type, func_body), module)
