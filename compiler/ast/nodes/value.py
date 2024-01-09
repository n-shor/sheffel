from ..types import VariableType

from . import Node


class Value(Node):
    """Represents any non-literal value creating statement."""
    def __init__(self, type_: VariableType):
        super().__init__()

        self.type_ = type_
