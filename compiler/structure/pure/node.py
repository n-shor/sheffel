from typing import Callable, Any


class Node:
    def hierarchy(self, prefix=''):
        fields = ''
        children = ''

        for name, value in self.__dict__.items():

            if name in self._omit_fields:
                continue

            if name in self._short_fields:
                fields += f'{name}={repr(value)}, '
                continue

            match value:
                case Node() as node:
                    children += '\n' + node.hierarchy(prefix + '\t')

                case (Node(), *_) as nodes:
                    children += ''.join('\n' + node.hierarchy(prefix + '\t') for node in nodes if node is not None)

                case _:
                    fields += f'{name}={repr(value)}, '

        fields = fields.rstrip(', ')

        return f'{prefix}{type(self).__name__}({fields}){children}'

    _omit_fields: set[str] = set()
    _short_fields: set[str] = set()

    def __repr__(self):

        attrs = []

        for name, value in self.__dict__.items():
            match value:
                case Node() | (Node(), *_):
                    attrs.append(f'{name}=...')
                case _:
                    attrs.append(f'{name}={value}')

        return f'{type(self).__name__}({', '.join(attrs)})'


class Block(Node):
    def __init__(self, nodes: tuple[Node, ...]):
        self.nodes = nodes
