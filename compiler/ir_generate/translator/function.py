from llvmlite import ir

from ...ast import nodes
from ...ast.types import VariableType, DirectUnqualifiedType, ValueMemoryQualifier

from .type_resolver import resolve as resolve_type
from .variable_scope import VariableScope


class Function(VariableScope):

    _symbol_id = 0

    def __init__(self, syntax: nodes.Function, module: ir.Module, symbol: str = ''):
        self.body = syntax.body
        self.module = module
        self.func = ir.Function(module, resolve_type(syntax.type_.base_type), symbol or self._get_unique_symbol())

        super().__init__(None, {param.name: arg for param, arg in zip(syntax.parameters, self.func.args)})

    @classmethod
    def _get_unique_symbol(cls):
        cls._symbol_id += 1
        return f'__function{cls._symbol_id}__'

    def translate(self):
        """Translates the function."""
        block.Block(self.body, self.func, self).translate()


def make_entry_function(module: ir.Module, body: nodes.Block):

    return_type = VariableType(DirectUnqualifiedType(ir.IntType(32)), ValueMemoryQualifier())
    func = nodes.Function(return_type, (), body)

    return Function(func, module, 'main')


from . import block
