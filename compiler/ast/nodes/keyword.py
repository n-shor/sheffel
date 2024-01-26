from dataclasses import dataclass

from . import Node


@dataclass
class Keyword(Node):
    """The base node for all keyword nodes."""


@dataclass
class Copy(Keyword):
    """Creates a copy of a variable."""

    copied: Node


@dataclass
class View(Keyword):
    """Creates a view of a variable."""

    viewed: Node


@dataclass
class Return(Keyword):
    """A terminator statement returning another statement."""

    returnee: Node


@dataclass
class ReturnVoid(Keyword):
    """A terminator statement returning void."""
