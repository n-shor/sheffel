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
