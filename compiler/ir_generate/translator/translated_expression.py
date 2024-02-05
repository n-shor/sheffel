from dataclasses import dataclass

from llvmlite import ir

from ...ast.types import VariableType, UnqualifiedType


@dataclass
class TranslatedExpression:

    label: ir.Value | ir.NamedValue
    type_: VariableType

    @classmethod
    def make_from_instruction(cls, instruction: ir.Instruction):
        return cls(instruction, instruction.type)
