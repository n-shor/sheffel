from llvmlite import ir

from ...ast.types import VariableType, DirectUnqualifiedType, MemoryQualifier, BehaviorQualifier


class Expression:
    """Represents a translated expression or statement with a type an ir representation."""

    def __init__(self, label: ir.Value | ir.NamedValue, type_: VariableType):
        self.label = label
        self.type_ = type_

    @classmethod
    def from_base_type_of(cls,
                          instruction: ir.Instruction,
                          memory_qualifier: MemoryQualifier, behavior_qualifiers: tuple[BehaviorQualifier, ...]
                          ):
        return cls(
            instruction,
            VariableType(DirectUnqualifiedType(instruction.type), memory_qualifier, behavior_qualifiers)
        )
