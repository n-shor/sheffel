from abc import ABCMeta, abstractmethod

from llvmlite import ir

from ...ast.types import VariableType, DirectUnqualifiedType, MemoryQualifier, BehaviorQualifier


class BaseExpression(metaclass=ABCMeta):
    """Represents a translated expression or statement with a type an ir representation."""

    @abstractmethod
    def label(self, builder: ir.IRBuilder) -> ir.Value:
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

    def label(self, builder):
        return self._label

    @property
    def type_(self):
        return self._type

    @classmethod
    def from_base_type_of(cls,
                          value: ir.Value,
                          memory_qualifier: MemoryQualifier, behavior_qualifiers: tuple[BehaviorQualifier, ...]
                          ):
        return cls(
            value,
            VariableType(DirectUnqualifiedType(value.type), memory_qualifier, behavior_qualifiers)
        )


class TerminatorExpression(Expression):
    pass
