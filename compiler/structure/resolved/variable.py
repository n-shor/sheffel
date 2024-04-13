from abc import ABCMeta, abstractmethod

from llvmlite import ir

from . import ValueOperationError, Scoped, Type, Value


class VariableOperationError(ValueOperationError):
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
    def copy_from(self, builder: ir.IRBuilder, other: Value):
        """Adds ir code which copies the value from another variable to this one."""
