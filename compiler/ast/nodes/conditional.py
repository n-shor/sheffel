from dataclasses import dataclass

from . import Node, Block


@dataclass
class IfConditional(Node):
    """Represents a conditional if statement."""

    condition: Node
    then: Block


@dataclass
class IfElseConditional(IfConditional):
    """Represents a conditional if statement which includes an else clause."""

    otherwise: Block
