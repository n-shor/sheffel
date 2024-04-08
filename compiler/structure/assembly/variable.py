from abc import ABCMeta, abstractmethod

from llvmlite import ir

from . import Scoped, Type


class Variable(Scoped, metaclass=ABCMeta):
    """Represents a value holding object."""

    @abstractmethod
    def declare(self, builder: ir.IRBuilder) -> None:
        """Adds ir code which declares the variable."""

    @abstractmethod
    def load(self, builder: ir.IRBuilder) -> ir.Value:
        """Adds ir code which loads data from the variable."""

    @abstractmethod
    def store(self, builder: ir.IRBuilder, value: ir.Value) -> None:
        """Adds ir code which stores data to the variable."""


class Evaluated(Variable):
    """Represents an eval variable; i.e. a compile time constant."""

    def __init__(self, value: ir.Value):
        self.value = value

    def declare(self, builder):
        pass

    def load(self, builder):
        return self.value

    def store(self, builder, value):
        raise TypeError(f"Evaluated variable with value='{self.value}' does not support modifications.")


class CopyVariable(Variable):
    """Represents a variable kept on the stack, which is always copied between uses."""

    def __init__(self, type_: Type):
        self.type_ = type_
        self._ptr: ir.NamedValue = None

    def declare(self, builder):
        self._ptr = builder.alloca(self.type_.ir_type)

    def load(self, builder):
        return builder.load(self._ptr)

    def store(self, builder, value):
        builder.store(value, self._ptr)
