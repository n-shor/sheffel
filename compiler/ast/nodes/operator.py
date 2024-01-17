from dataclasses import dataclass

from . import Node


@dataclass
class Operator(Node):
    """Represents a call to an operator, which is a function defined by a symbol."""

    signature: str
    operands: tuple[Node]
