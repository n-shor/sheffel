from __future__ import annotations

from llvmlite import ir

from . import CompilationError, Scoped, Value
from .values import EvalValue


class UnresolvedOperatorError(CompilationError):
    """Raised when attempting to use an undefined operator of a type or one of mismatching types."""


class Type(EvalValue, Scoped):
    def __init__(self, meta: Type, ir_type: ir.Type, name_hint=''):
        EvalValue.__init__(self, meta, self, None)
        Scoped.__init__(self, name_hint)
        self.ir_type = ir_type

    def operator(self, builder: ir.IRBuilder, operation: str, operands: tuple[Value, ...]) -> Value:
        """Adds proper instructions to execute an operator of a value of this type."""
        raise UnresolvedOperatorError(f'Operation {repr(operation)} on {operands} '
                                      f'cannot be resolved by type {self.get_name()}.')
