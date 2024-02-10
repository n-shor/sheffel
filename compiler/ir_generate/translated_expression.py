from dataclasses import dataclass

from llvmlite import ir

from ..ast.types import VariableType, DirectUnqualifiedType, MemoryQualifier, BehaviorQualifier


@dataclass
class TranslatedExpression:

    label: ir.Value | ir.NamedValue
    type_: VariableType

    @classmethod
    def type_from_instruction(cls, instruction: ir.Instruction, memory_qualifier: MemoryQualifier, behavior_qualifiers: tuple[BehaviorQualifier]):
        return cls(
            instruction,
            VariableType(DirectUnqualifiedType(instruction.type), memory_qualifier, behavior_qualifiers)
        )
