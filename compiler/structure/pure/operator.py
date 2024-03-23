from . import Node, Value


class Operator(Node):
    def __init__(self, operation: str, operands: tuple[Value, ...]):
        self.operation = operation
        self.operands = operands
