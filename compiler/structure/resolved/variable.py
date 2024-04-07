from __future__ import annotations

from llvmlite import ir

from . import Node


class Variable(Node):
    def __init__(self, name: str, ir_type: ir.Type):
        self.name = name
        self.ir_type = ir_type

    def syntax(self):
        return f'{self.name}:{self.ir_type}'


class VariableDeclaration(Variable):
    def syntax(self):
        return f'declare {super().syntax()}'


class VariableGet(Variable):
    def syntax(self):
        return f'get {super().syntax()}'
