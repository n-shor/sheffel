from dataclasses import dataclass

from . import Node


@dataclass
class Block(Node):
    """Represents a block of code made of several lines. This is effectively a scope."""

    statements: tuple[Node]
