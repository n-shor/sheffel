from ..types import FunctionType, VariableType, ReferenceMemoryQualifier

from . import Node, Value, Block, VariableDeclaration


class Function(Value):
    """Represents a function creating statement. The function has a type and body."""
    def __init__(self, return_type: VariableType, parameters: tuple[VariableDeclaration, ...], body: Block):
        super().__init__(VariableType(
            FunctionType(return_type, tuple(p.type_ for p in parameters)),
            ReferenceMemoryQualifier()
        ))

        self.parameters = parameters
        self.body = body


class Return(Node):
    """A terminator statement returning another statement."""
    def __init__(self, returnee: Node):
        super().__init__()

        self.returnee = returnee
