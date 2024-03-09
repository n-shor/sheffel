from __future__ import annotations

from enum import Enum

from . import Node, Block


class Memory(Enum):
    EVAL = 0,
    COPY = 1,
    REF = 2


class Value(Node):
    def __init__(self, type_: Type, memory: Memory):
        self.type_ = type_
        self.memory = memory


class Type(Value):
    def __init__(self, meta: Value, body: Block):
        super().__init__(meta.type_, Memory.EVAL)
        self.body = body


class _TypeType(Type):
    def __init__(self):
        self.type_ = self  # allows the magic of self instantiation without infinite recursion
        super().__init__(self, Block(()))


type_type = _TypeType()
