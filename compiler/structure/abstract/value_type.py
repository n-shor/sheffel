from __future__ import annotations

from . import Node, Block


class Value(Node):
    def __init__(self, type_: Type):
        self.type_ = type_


class Type(Value):
    def __init__(self, meta: Type, body: Block):
        super().__init__(meta)
        self.body = body


class _TypeType(Type):
    def __init__(self):
        super().__init__(self, Block(()))

    def __repr__(self):
        return 'type_type'


type_type = _TypeType()
