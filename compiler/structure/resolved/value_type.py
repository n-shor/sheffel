from __future__ import annotations
from abc import ABCMeta, abstractmethod

from llvmlite import ir
from . import Scoped, CompilationError


class UnresolvedOperatorError(CompilationError):
    """Raised when attempting to use an undefined operator of a type or one of mismatching types."""


class Value(metaclass=ABCMeta):

    def __init__(self, type_: Type):
        self.type_ = type_

    @abstractmethod
    def load(self, builder: ir.IRBuilder) -> ir.Constant | ir.NamedValue:
        """Adds ir code which loads data from this value."""


class Type(Scoped):
    def __init__(self, ir_type: ir.Type, name_hint=''):
        super().__init__(name_hint)
        self.ir_type = ir_type

    def operator(self, builder: ir.IRBuilder, operation: str, operands: tuple[Value, ...]) -> Value:
        """Adds proper instructions to execute an operator of a value of this type."""
        raise UnresolvedOperatorError(f'Operation {repr(operation)} on {operands} '
                                      f'cannot be resolved by type {self.get_name()}.')
