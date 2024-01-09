from abc import ABC, abstractmethod
from typing import Callable

from llvmlite import ir


class UnqualifiedType(ABC):
    """The base for unqualified type information."""

    @abstractmethod
    def get_direct(self, resolver: Callable[[str], ir.Type]) -> ir.Type:
        """Gets the direct type (llvmlite.ir correspondent) of the current type."""
        ...


class NamedUnqualifiedType(UnqualifiedType):
    """An unqualified type represented by a string of its name."""
    def __init__(self, name: str):
        super().__init__()

        self.name = name

    def get_direct(self, resolver: Callable[[str], ir.Type]) -> ir.Type:
        return resolver(self.name)


class DirectUnqualifiedType(UnqualifiedType):
    """An unqualified type represented by its llvmlite.ir correspondent."""
    def __init__(self, type_: ir.Type):
        super().__init__()

        self.type_ = type_

    def get_direct(self, resolver: Callable[[str], ir.Type]) -> ir.Type:
        return self.type_
