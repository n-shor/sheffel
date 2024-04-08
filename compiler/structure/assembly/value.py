from abc import ABCMeta, abstractmethod

from llvmlite import ir


class Value(metaclass=ABCMeta):
    @abstractmethod
    def load(self, builder: ir.IRBuilder) -> ir.Value:
        """Adds ir code which loads data from this value."""


class LiteralValue(Value):
    def __init__(self, value: ir.Value):
        self.value = value

    def load(self, builder):
        return self.value
