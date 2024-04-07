from __future__ import annotations

from llvmlite import ir

from . import Node


class Expression(Node):
    def __init__(self, type_: Type):
        self.type_ = type_


class Type(Expression):
    def __init__(self, meta: Type, ir_type: ir.Type):
        super().__init__(meta)
        self.ir_type = ir_type


class TypeType(Type):
    def __init__(self):
        super().__init__(self, ir.VoidType())
