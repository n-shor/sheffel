from __future__ import annotations

from .options import MemoryQualifier, Passer


class Node:
    def hierarchy(self, prefix=''):
        subtext = ''

        for name, value in self.__dict__.items():
            match value:
                case Node() as node:
                    subtext += '\n' + node.hierarchy(prefix + '\t')
                case (Node(), *_) as nodes:
                    subtext += ''.join('\n' + node.hierarchy(prefix + '\t') for node in nodes)

        return f'{prefix}{self}{subtext}'

    def __repr__(self):

        attrs = []

        for name, value in self.__dict__.items():
            match value:
                case Node() | (Node(), *_):
                    pass
                case _:
                    attrs.append(f'{name}={value}')

        return f'{type(self).__name__}({', '.join(attrs)})'


class Block(Node):
    def __init__(self, nodes: tuple[Node, ...]):
        self.nodes = nodes


class Declaration(Node):
    def __init__(self, type_: QualifiedType, name: str):
        self.type_ = type_
        self.name = name


class Assignment(Node):
    def __init__(self, name: str, value: Value):
        self.name = name
        self.value = value


class DeclarationAssignment(Node):
    def __init__(self, type_: QualifiedType, name: str, value: Value):
        self.type_ = type_
        self.name = name
        self.value = value


class Value(Node):
    def __init__(self, passer: Passer = Passer.IMPLICIT):
        self.passer = passer


class Type(Value):
    def __init__(self, fields: dict[Declaration | DeclarationAssignment]):
        super().__init__()
        self.fields = fields


class QualifiedType:
    def __init__(self, type_: Type, memory_qualifier: MemoryQualifier):
        self.type_ = type_
        self.memory_qualifier = memory_qualifier


class Function(Value):
    def __init__(self, return_type: Type, argument_types: tuple[Type], body: Block):
        super().__init__()
        self.return_type = return_type
        self.argument_types = argument_types
        self.body = body


class Array(Value):
    def __init__(self, type_: QualifiedType, values: tuple[Value, ...]):
        super().__init__()
        self.type_ = type_
        self.values = values

























