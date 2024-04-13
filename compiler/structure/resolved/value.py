from __future__ import annotations
from abc import ABCMeta, abstractmethod

from llvmlite import ir


class Value(metaclass=ABCMeta):

    def __init__(self, type_: 'Type'):
        self.type_ = type_

    @abstractmethod
    def load(self, builder: ir.IRBuilder) -> ir.Constant | ir.NamedValue:
        """Adds ir code which loads data from this value."""

    @abstractmethod
    def ptr(self, builder: ir.IRBuilder) -> ir.NamedValue:
        """Returns a pointer to the value."""
