from dataclasses import dataclass

from . import Node


@dataclass
class IfConditional(Node):
    """Represents a conditional if statement."""

    condition: Node
    on_true: Node


@dataclass
class IfElseConditional(IfConditional):
    """Represents a conditional if statement which includes an else clause."""

    on_false: Node
