from __future__ import annotations

from llvmlite import ir

from . import Named


class _Variable(Named):
    def __init__(self, name: str, ir_type: ir.Type):
        super().__init__(name)
        self.ir_type = ir_type

    def syntax(self):
        return f'{super().syntax()}:{self.ir_type}'


class VariableDeclaration(_Variable):
    def syntax(self):
        return f'declare {super().syntax()}'


class VariableSet(_Variable):
    def syntax(self):
        return f'set {super().syntax()}'


class VariableGet(_Variable):
    def syntax(self):
        return f'get {super().syntax()}'
