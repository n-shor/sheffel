class Node:
    pass


class Literal(Node):
    def __init__(self):
        super().__init__()


class NumericLiteral(Literal):
    def __init__(self):
        super().__init__()


class IntegralLiteral(NumericLiteral):
    def __init__(self, value: int):
        super().__init__()

        self.value = value


class FloatingLiteral(NumericLiteral):
    def __init__(self, value: float):
        super().__init__()

        self.value = value


class StringLiteral(Literal):
    def __init__(self, value: str):
        super().__init__()

        self.value = value


class Operator(Node):
    def __init__(self, signature: str, *operands: Node):
        super().__init__()

        self.signature = signature
        self.operands = operands


class UnaryOperator(Operator):
    def __init__(self, signature: str, operand: Node):
        super().__init__(signature, operand)


class BinaryOperator(Operator):
    def __init__(self, signature: str, left: Node, right: Node):
        super().__init__(signature, left, right)
