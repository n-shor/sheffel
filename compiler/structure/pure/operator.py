from . import Node


class Operator(Node):
    def __init__(self, operation: str, operands: tuple[Node, ...]):
        self.operation = operation
        self.operands = operands
