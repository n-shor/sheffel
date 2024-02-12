from abc import ABCMeta, abstractmethod

from llvmlite import ir

from ...ast.types import VariableType, DirectUnqualifiedType, MemoryQualifier, BehaviorQualifier


class BaseExpression(metaclass=ABCMeta):
    """Represents a translated expression or statement with a type an ir representation."""

    @property
    @abstractmethod
    def label(self) -> ir.Value:
        """The instruction the expression represents."""

    @property
    @abstractmethod
    def type_(self) -> VariableType:
        """The type of the expression."""


class Expression(BaseExpression):
    """Represents a translated expression or statement with a type an ir representation."""

    def __init__(self, label: ir.Value, type_: VariableType):
        self._label = label
        self._type = type_

    @property
    def label(self):
        return self._label

    @property
    def type_(self):
        return self._type

    @classmethod
    def from_base_type_of(cls,
                          instruction: ir.Instruction,
                          memory_qualifier: MemoryQualifier, behavior_qualifiers: tuple[BehaviorQualifier, ...]
                          ):
        return cls(
            instruction,
            VariableType(DirectUnqualifiedType(instruction.type), memory_qualifier, behavior_qualifiers)
        )
