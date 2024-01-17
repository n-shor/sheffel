from dataclasses import dataclass

from typing import Any

from ..types import LiteralType

from . import Node


@dataclass
class Literal(Node):
    """Represents a literal value."""

    value: Any
    type_: LiteralType
