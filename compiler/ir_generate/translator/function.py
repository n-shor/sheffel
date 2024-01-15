from llvmlite import ir

from ...ast import nodes
from ...ast.types import FunctionType, VariableType, DirectUnqualifiedType, ValueMemoryQualifier

from .type_resolver import resolve as resolve_type


class Function:

    _symbol_id = 0

    def __init__(self, syntax: nodes.Function, module: ir.Module, symbol: str = ''):
        self.body = syntax.body
        self.module = module
        self.func = ir.Function(module, resolve_type(syntax.type_.base_type), symbol or self._get_unique_symbol())

    @classmethod
    def _get_unique_symbol(cls):
        cls._symbol_id += 1
        return f'__function{cls._symbol_id}__'

    def translate(self):
        """Translates the function."""
        block.Block(self.body, self.func).translate()


def make_entry_function(module: ir.Module, body: nodes.Block):

    return_type = VariableType(DirectUnqualifiedType(ir.IntType(32)), ValueMemoryQualifier())
    func_type = FunctionType(return_type=return_type)
    func = nodes.Function(func_type, body)

    return Function(func, module, 'main')


from . import block
