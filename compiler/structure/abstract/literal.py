from llvmlite import ir

from . import Node


class Literal(Node):
    def __init__(self, value: ir.Value):
        self.value = value

    def syntax(self):
        return f'{self.value}'
