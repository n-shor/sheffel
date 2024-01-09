from . import Node


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
