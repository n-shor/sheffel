class Node:
    pass

class Number(Node):
    def __init__(self):
        super().__init__()

class IntegralNumber(Number):
    def __init__(self, value: int):
        super().__init__()
        
        self.value = value

class FloatingNumber(Number):
    def __init__(self, value: float):
        super().__init__()
        
        self.value = value

class Operator(Node):
    def __init__(self, signature: str, *operands: Node):
        super().__init__()
        
        self.signature = signature
        self.operands = operands

class UnaryOperator(Node):
    def __init__(self, signature: str, operand: Node):
        super().__init__(signature, operand)

class BinaryOperator(Node):
    def __init__(self, signature: str, left: Node, right: Node):
        super().__init__(signature, left, right)