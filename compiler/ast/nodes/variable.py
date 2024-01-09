from ..types import VariableType

from . import Node


class Variable(Node):
    """Represents any reference to a variable name."""
    def __init__(self, name: str):
        super().__init__()

        self.name = name


class ReadVariable(Variable):
    """Represents any read from a variable name."""
    def __init__(self, name: str):
        super().__init__(name)


class WriteVariable(Variable):
    """Represents any write to a variable name."""
    def __init__(self, name: str):
        super().__init__(name)


class VariableDeclaration(WriteVariable):
    """Represents a declaration of a variable."""
    def __init__(self, name: str, type_: VariableType):
        super().__init__(name)

        self.type_ = type_
