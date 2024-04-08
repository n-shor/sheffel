from enum import Enum

from . import Node, Value


class Memory(Enum):
    EVAL = '^'
    COPY = '&'
    REF = '*'


class MemoryComposition(Node):
    def __init__(self, memory: Memory, type_: Value):
        self.memory = memory
        self.type_ = type_

    def syntax(self):
        return f'{self.memory.value}{self.type_.syntax()}'
