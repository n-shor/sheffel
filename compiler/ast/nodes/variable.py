from dataclasses import dataclass

from ..types import VariableType

from . import Node


@dataclass
class Variable(Node):
    """Represents any reference to a variable name."""

    name: str


@dataclass
class ReadVariable(Variable):
    """Represents any read from a variable name."""


@dataclass
class WriteVariable(Variable):
    """Represents any write to a variable name."""


@dataclass
class VariableDeclaration(WriteVariable):
    """Represents a declaration of a variable."""
    type_: VariableType
