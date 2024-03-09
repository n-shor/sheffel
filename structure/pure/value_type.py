from __future__ import annotations

from enum import Enum

from . import Node, Block


class Memory(Enum):
    EVAL = 0,
    COPY = 1,
    REF = 2


class Value(Node):
    def __init__(self, qualified: Qualified):
        self.qualified = qualified


class Qualified(Value):
    def __init__(self, type_: Type, memory: Memory, *, base=False):
        super().__init__(self if base else eval_type_type)
        self.type_ = type_
        self.memory = memory


class Type(Node):
    def __init__(self, meta: Qualified, body: Block):
        self.meta = meta
        self.body = body


class _TypeType(Type):
    def __init__(self):
        super().__init__(eval_type_type, Block(()))


eval_type_type = Qualified(None, Memory.EVAL, base=True)
eval_type_type.type_ = _TypeType()
