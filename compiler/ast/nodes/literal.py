from ..types import LiteralType

from . import Node


class Literal(Node):
    """Represents a literal value."""
    def __init__(self, value, type_: LiteralType):
        super().__init__()

        self.value = value
        self.type_ = type_
