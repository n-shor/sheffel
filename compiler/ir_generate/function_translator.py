from llvmlite import ir

from compiler.ast.nodes import Block, Function
from compiler.ast.types import VariableType, DirectUnqualifiedType, ValueMemoryQualifier


from . import resolve_type, Scope
from .translated.variable import Parameter


class FunctionTranslator(Scope):

    _symbol_id = 0

    def __init__(self, syntax: Function, module: ir.Module, name: str = ''):
        self.module = module
        self.syntax = syntax
        self.func = ir.Function(module, resolve_type(syntax.type_.base_type), module.get_unique_name(name))

        super().__init__(
            None,
            {param.name: Parameter(arg, param.type_.base_type) for param, arg in zip(syntax.parameters, self.func.args)}
        )

    def translate(self):
        """Translates the function."""
        return BlockTranslator(ir.IRBuilder(self.func.append_basic_block()), self).translate(self.syntax.body)


def make_entry_function(module: ir.Module, body: Block):

    return_type = VariableType(DirectUnqualifiedType(ir.IntType(32)), ValueMemoryQualifier(), ())
    syntax = Function.make(return_type, (), body)

    return FunctionTranslator(syntax, module, 'main')


from .block_translator import BlockTranslator
