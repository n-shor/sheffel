from ..types import FunctionType, VariableType, ReferenceMemoryQualifier, ConstBehaviorQualifier

from . import Node, Value


class Block(Node):
    """Represents a block of code made of several lines. This is effectively a scope."""
    def __init__(self, *statements: Node):
        super().__init__()

        self.statements = statements


class Function(Value):
    """Represents a function creating statement."""
    def __init__(self, type_: FunctionType, *blocks: Block):
        super().__init__(VariableType(type_.get_direct_unqualified_type(), ReferenceMemoryQualifier(), ConstBehaviorQualifier()))

        self.type_ = type_
        self.blocks = blocks
