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


@dataclass
class Break(Node):
    """A statement immediately terminating a loop."""


@dataclass
class Break(Node):
    """A statement immediately ending a loop's body."""


@dataclass
class Return(Node):
    """A terminator statement returning another statement."""

    returnee: Node


@dataclass
class ReturnVoid(Node):
    """A terminator statement returning void."""
