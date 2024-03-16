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
    _as_field = True

    def __init__(self, type_: Type | Variable, memory: Memory, *, base=False):
        super().__init__(self if base else eval_type_type)
        self.type_ = type_
        self.memory = memory

    def __repr__(self):
        return f'{type(self).__name__}({repr(self.type_)}, {self.memory})'


class Type(Node):
    def __init__(self, meta: Qualified, body: Block):
        self.meta = meta
        self.body = body


class _TypeType(Type):
    _as_field = True

    def __init__(self):
        super().__init__(eval_type_type, Block(()))

    def __repr__(self):
        return f'{type(self).__name__}()'


eval_type_type = Qualified(None, Memory.EVAL, base=True)
eval_type_type.type_ = _TypeType()


class Literal(Value):
    def __init__(self, type_: Type, value):
        super().__init__(Qualified(type_, Memory.EVAL))
        self.value = value


class Variable(Node):
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f'{type(self).__name__}({repr(self.name)})'


class Declaration(Variable):
    def __init__(self, qualified: Qualified, name: str):
        self.qualified = qualified
        super().__init__(name)
