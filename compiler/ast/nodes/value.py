from ..types import VariableType, FunctionType, ConstBehaviorQualifier, ReferenceMemoryQualifier

from .node import Node
from .flow_control import Block


class Value(Node):
    """Represents any non-literal value creating statement."""
    def __init__(self, type_: VariableType):
        super().__init__()

        self.type_ = type_


class Function(Value):
    """Represents a function creating statement."""
    def __init__(self, type_: FunctionType, *blocks: Block):
        super().__init__(VariableType(type_.get_direct_unqualified_type(), ReferenceMemoryQualifier(), ConstBehaviorQualifier()))

        self.type_ = type_
        self.blocks = blocks
