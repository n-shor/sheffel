from dataclasses import dataclass

from . import Node, Return, ReturnVoid


@dataclass
class Block(Node):
    """Represents a block of code made of several lines. This is effectively a scope."""

    statements: tuple[Node, ...]

    def returns(self):
        """Whether the block returns."""
        return any(isinstance(statement, (Return, ReturnVoid)) for statement in self.statements)
