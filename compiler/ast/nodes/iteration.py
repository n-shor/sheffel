from dataclasses import dataclass

from . import Node, Block


@dataclass
class While(Node):
    """Represents a while loop."""

    condition: Node
    body: Block
