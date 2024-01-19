from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable

from llvmlite import ir


@dataclass
class UnqualifiedType(ABC):
    """The base for unqualified type information."""

    @abstractmethod
    def get_direct(self, resolver: Callable[[str], ir.Type]) -> ir.Type:
        """Gets the direct type (llvmlite.ir correspondent) of the current type."""
        ...


@dataclass
class NamedUnqualifiedType(UnqualifiedType):
    """An unqualified type represented by a string of its name."""

    name: str

    def get_direct(self, resolver: Callable[[str], ir.Type]):
        return resolver(self.name)


@dataclass
class DirectUnqualifiedType(UnqualifiedType):
    """An unqualified type represented by its llvmlite.ir correspondent."""

    type_: ir.Type

    def get_direct(self, resolver: Callable[[str], ir.Type]):
        return self.type_


@dataclass
class UnknownUnqualifiedType(UnqualifiedType):
    """An unqualified type with an unknown value. Its value is decided in a later compilation step."""

    def get_direct(self, resolver: Callable[[str], ir.Type]) -> ir.Type:
        raise TypeError(f'{type(self)} cannot be viewed directly.')
