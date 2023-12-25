from llvmlite import ir


class Node:
    """A base node for representing any operation."""
    pass


class Literal(Node):
    """Represents a literal value."""
    def __init__(self):
        super().__init__()


class NumericLiteral(Literal):
    """Represents a numeric literal value."""
    def __init__(self):
        super().__init__()


class IntegralLiteral(NumericLiteral):
    """Represents any negative or positive integer literal value."""
    def __init__(self, value: int):
        super().__init__()

        self.value = value


class FloatingLiteral(NumericLiteral):
    """Represents any floating point literal value."""
    def __init__(self, value: float):
        super().__init__()

        self.value = value


class StringLiteral(Literal):
    """Represents a literal string value."""
    def __init__(self, value: str):
        super().__init__()

        self.value = value


class Variable(Node):
    """Represents any reference to a variable name."""
    def __init__(self, name: str):
        super().__init__()

        self.name = name


class VariableDeclaration(Variable):
    """Represents a declaration of a variable."""
    def __init__(self, name: str, value_type: ir.Type):
        super().__init__(name)

        self.value_type = value_type


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
