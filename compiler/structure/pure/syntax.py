from __future__ import annotations

from . import Node, Memory, Value, Qualified, Type


class Literal(Value):
    def __init__(self, type_: Type, value):
        super().__init__(Qualified(type_, Memory.EVAL))
        self.value = value


class Variable(Node):
    def __init__(self, name: str):
        self.name = name


class Declaration(Variable):
    def __init__(self, qualified: Qualified, name: str):
        super().__init__(name)
        self.qualified = qualified


class Operator(Node):
    def __init__(self, operation: str, operands: tuple[Node, ...]):
        self.operation = operation
        self.operands = operands
