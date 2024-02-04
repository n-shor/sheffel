from dataclasses import dataclass

from . import Node


@dataclass
class Copy(Node):
    """Creates a copy of a variable."""

    copied: Node


@dataclass
class View(Node):
    """Creates a view of a variable."""

    viewed: Node
