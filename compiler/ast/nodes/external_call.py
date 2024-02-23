from dataclasses import dataclass

from . import Node


@dataclass
class ExternalCall(Node):
    """Calls a named external."""

    external_name: str
    parameters: tuple[Node, ...]
