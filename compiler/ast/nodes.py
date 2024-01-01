from .types.function_type import FunctionType
from .types.variable_type import VariableType
from .types.literal_type import LiteralType

from .types.memory_qualifiers import ValueMemoryQualifier, ReferenceMemoryQualifier
from .types.behavior_qualifiers import ConstBehaviorQualifier, NoWriteBehaviorQualifier, NoReadBehaviorQualifier


class Node:
    """A base node for representing any operation."""


class Literal(Node):
    """Represents a literal value."""
    def __init__(self, value, type_: LiteralType):
        super().__init__()

        self.value = value
        self.type_ = type_


class Operator(Node):
    """Represents a call to an operator: a function defined by a symbol."""
    def __init__(self, signature: str, *operands: Node):
        super().__init__()

        self.signature = signature
        self.operands = operands


class UnaryOperator(Operator):
    """Represents a call to an operator accepting a single argument."""
    def __init__(self, signature: str, operand: Node):
        super().__init__(signature, operand)


class BinaryOperator(Operator):
    """Represents a call to an operator accepting two arguments: one to its left and one to its right."""
    def __init__(self, signature: str, left: Node, right: Node):
        super().__init__(signature, left, right)


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


class Return(Node):
    """Represents a return call."""
    def __init__(self, returnee: Node):
        super().__init__()

        self.returnee = returnee


class Block(Node):
    """Represents a block of code made of several lines."""
    def __init__(self, *lines: Node):
        super().__init__()

        self.lines = lines


class Value(Node):
    """Represents any non-literal value."""
    def __init__(self, type_: VariableType):
        super().__init__()

        self.type_ = type_


class Function(Value):
    """Represents a function creating statement."""
    def __init__(self, block: Block, type_: FunctionType):
        super().__init__(VariableType(type_.get_direct_unqualified_type(), ReferenceMemoryQualifier(), ConstBehaviorQualifier()))

        self.block = block
        self.type_ = type_
