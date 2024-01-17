from dataclasses import dataclass

from ..types import VariableType

from . import Node


@dataclass
class Value(Node):
    """Represents any non-literal value creating statement."""

    type_: VariableType
