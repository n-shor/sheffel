from __future__ import annotations
from abc import ABCMeta, abstractmethod

from llvmlite import ir


class Value(metaclass=ABCMeta):

    def __init__(self, type_: Type):
        self.type_ = type_

    @abstractmethod
    def load(self, builder: ir.IRBuilder) -> ir.Value:
        """Adds ir code which loads data from this value."""


class LiteralValue(Value):
    def __init__(self, type_: Type, py_value, ir_value: ir.Value):
        super().__init__(type_)
        self._py_value = py_value
        self._ir_value = ir_value

    def value(self):
        """Returns the python equivalent to the value."""
        return self._py_value

    def load(self, builder):
        return self._ir_value


from .type import Type
