from dataclasses import dataclass
from typing import Callable

from llvmlite import ir

from .unqualified_type import UnqualifiedType, DirectUnqualifiedType
from .qualifiers import BehaviorQualifier, MemoryQualifier, ValueMemoryQualifier


@dataclass
class VariableType(UnqualifiedType):
    """The qualified type information of a variable."""

    base_type: UnqualifiedType
    memory: MemoryQualifier
    behavior: tuple[BehaviorQualifier, ...]

    def get_direct(self, resolver: Callable[[str], ir.Type]) -> ir.Type:
        return self.base_type.get_direct(resolver)


class VoidType(VariableType):
    """The information of a stateless type."""
    def __init__(self):
        super().__init__(DirectUnqualifiedType(ir.VoidType()), ValueMemoryQualifier(), ())

    def __repr__(self):
        return type(self).__name__
