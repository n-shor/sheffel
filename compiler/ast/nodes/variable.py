from dataclasses import dataclass

from ..types import VariableType

from . import Node


@dataclass
class Variable(Node):
    """Represents any reference to a variable name."""

    name: str


@dataclass
class VariableDeclaration(Variable):
    """Represents a declaration of a variable."""
    type_: VariableType
