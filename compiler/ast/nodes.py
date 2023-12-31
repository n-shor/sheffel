from .types import CompleteType, LiteralType


class Node:
    """A base node for representing any operation."""


class Literal(Node):
    """Represents a literal value."""
    def __init__(self, value, type_: LiteralType):
        super().__init__()

        self.value = value
        self.type_ = type_


class NumericLiteral(Literal):
    """Represents a numeric literal value."""
    def __init__(self, value, type_: LiteralType):
        super().__init__(value, type_)


class IntegralLiteral(NumericLiteral):
    """Represents any negative or positive integer literal value."""
    def __init__(self, value: int):
        super().__init__(value, LiteralType('Int'))


class FloatingLiteral(NumericLiteral):
    """Represents any floating point literal value."""
    def __init__(self, value: float):
        super().__init__(value, LiteralType('Float'))


class StringLiteral(Literal):
    """Represents a literal string value."""
    def __init__(self, value: str):
        super().__init__(value, LiteralType('String'))


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
    def __init__(self, name: str, type_: CompleteType):
        super().__init__(name)

        self.type_ = type_
