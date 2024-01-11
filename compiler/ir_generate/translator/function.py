from llvmlite import ir

from ...ast import nodes
from ...ast.types import FunctionType, VariableType, DirectUnqualifiedType, ValueMemoryQualifier

from .type_resolver import resolve as resolve_type


class Function:
    def __init__(self, syntax: nodes.Function, module: ir.Module, symbol: str = None):
        self.body = syntax.body
        self.module = module
        self.func = ir.Function(module, resolve_type(syntax.type_), symbol)

    def translate(self):
        """Translates the function."""
        Block(self.body, self.func).translate()


def make_entry_function(module: ir.Module, body: nodes.Block):

    return_type = VariableType(DirectUnqualifiedType(ir.IntType(32)), ValueMemoryQualifier())
    func_type = FunctionType(return_type=return_type)
    func = nodes.Function(func_type, body)

    return Function(func, module, 'main')


from .block import Block
