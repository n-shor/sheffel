from __future__ import annotations

from llvmlite import ir

from . import CompilationError, Scoped


class UnresolvedOperatorError(CompilationError):
    """Raised when attempting to use an undefined operator of a type or one of mismatching types."""


class Type(Scoped):
    def __init__(self, ir_type: ir.Type, name_hint=''):
        super().__init__(name_hint)
        self.ir_type = ir_type

    def operator(self, builder: ir.IRBuilder, operation: str, operands: tuple[Value, ...]) -> Value:
        """Adds proper instructions to execute an operator of a value of this type."""
        raise UnresolvedOperatorError(f'Operation {repr(operation)} on {operands} '
                                      f'cannot be resolved by type {self.get_name()}.')


from .value import Value
