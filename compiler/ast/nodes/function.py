from ..types import FunctionType, VariableType, ReferenceMemoryQualifier, ConstBehaviorQualifier

from . import Node, Value, Block


class Function(Value):
    """Represents a function creating statement. The function has a type and body."""
    def __init__(self, type_: FunctionType, body: Block):
        super().__init__(VariableType(type_, ReferenceMemoryQualifier(), ConstBehaviorQualifier()))

        self.body = body


class Return(Node):
    """A terminator statement returning another statement."""
    def __init__(self, returnee: Node):
        super().__init__()

        self.returnee = returnee
