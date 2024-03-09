from __future__ import annotations

from . import Node, Memory, Value


class Variable(Node):
    def __init__(self, name: str):
        self.name = name


class Declaration(Variable):
    def __init__(self, type_: Value, memory: Memory, name: str):
        super().__init__(name)
        self.type_ = type_
        self.memory = memory


class Operator(Node):
    def __init__(self, operation: str, operands: tuple[Node, ...]):
        self.operation = operation
        self.operands = operands
