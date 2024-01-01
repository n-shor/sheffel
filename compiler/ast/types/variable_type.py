from .behavior_qualifiers import BehaviorQualifier
from .memory_qualifiers import MemoryQualifier
from .unqualified_type import UnqualifiedType


class VariableType:
    """The qualified type information of a variable."""
    def __init__(self, base_type: UnqualifiedType, memory: MemoryQualifier, *behavior: BehaviorQualifier):
        self.base_type = base_type
        self.memory = memory
        self.behavior = behavior
