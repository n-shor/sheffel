from abc import ABCMeta, abstractmethod

from llvmlite import ir

from . import CompilationError, Scoped, Type, Value


class VariableOperationError(CompilationError):
    """An unsupported operation on a variable."""


class Variable(Value, Scoped, metaclass=ABCMeta):
    """Represents a value holding object."""

    def __init__(self, type_: Type, name_hint=''):
        Value.__init__(self, type_)
        Scoped.__init__(self, name_hint)

    @abstractmethod
    def declare(self, builder: ir.IRBuilder) -> None:
        """Adds ir code which declares the variable."""

    @abstractmethod
    def get_ptr(self, builder: ir.IRBuilder) -> ir.NamedValue:
        """Returns a pointer to the variable's value"""

    @abstractmethod
    def store(self, builder: ir.IRBuilder, value: ir.Value) -> None:
        """Adds ir code which stores data to the variable."""
