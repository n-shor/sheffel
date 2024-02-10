from dataclasses import dataclass

from . import Node, Block


@dataclass
class IfConditional(Node):
    """Represents a conditional if statement."""

    condition: Node
    then: Node


@dataclass
class IfElseConditional(IfConditional):
    """Represents a conditional if statement which includes an else clause."""

    otherwise: Node
