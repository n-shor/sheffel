from typing import Callable

from llvmlite import ir

from . import UnqualifiedType, BehaviorQualifier, MemoryQualifier


class VariableType(UnqualifiedType):
    """The qualified type information of a variable."""
    def __init__(self, base_type: UnqualifiedType, memory: MemoryQualifier, *behavior: BehaviorQualifier):
        super().__init__()

        self._type = base_type
        self.memory = memory
        self.behavior = behavior

    def get_direct(self, resolver: Callable[[str], ir.Type]) -> ir.Type:
        return self._type.get_direct(resolver)
