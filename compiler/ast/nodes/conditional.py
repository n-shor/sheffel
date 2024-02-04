from dataclasses import dataclass

from . import Node


@dataclass
class Conditional(Node):
    """Represents a conditional if statement."""

    condition: Node
    on_true: Node
    on_false: Node
