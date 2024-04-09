from enum import Enum

from . import Node, Block


class Memory(Enum):
    EVAL = '^'
    COPY = '&'
    REF = '*'


class MemoryComposition(Node):
    def __init__(self, memory: Memory, type_: Node):
        self.memory = memory
        self.type_ = type_

    def syntax(self):
        return f'{self.memory.value}{self.type_.syntax()}'


class ArrayComposition(Node):
    def __init__(self, element_type: Node, values: tuple[Node, ...]):
        self.element_type = element_type
        self.values = values

    def syntax(self):
        return f'{self.element_type.syntax()}[{', '.join(value.syntax() for value in self.values)}]'


class FunctionComposition(Node):
    def __init__(self, return_type: Node, arguments: tuple[Node, ...], body: Block):
        self.return_type = return_type
        self.arguments = arguments
        self.body = body

    def syntax(self):
        return f'{self.return_type.syntax()}({', '.join(argument.syntax() for argument in self.arguments)}) {self.body.syntax()}'
