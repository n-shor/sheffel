class Node:

    _as_field = False

    def _categorise_attrs(self):
        """Yields attrs in the following format: (is_node, name, value)"""

        for name, value in self.__dict__.items():
            match value:
                case Node(_as_field=True):
                    yield False, name, value

                case Node():
                    yield True, name, value

                case [*values] if len(values) > 0 and all(isinstance(value, Node) for value in values):
                    for node in values:
                        yield True, name, node

                case _:
                    yield False, name, value

    def fields(self):
        return f'{type(self).__name__}({', '.join(
            f'{name}={repr(value)}' for is_node, name, value in self._categorise_attrs() if not is_node
        )})'

    def hierarchy(self, prefix=''):
        return f'{prefix}{self.fields()}\n{''.join(
            value.hierarchy(prefix + '\t') for is_node, name, value in self._categorise_attrs() if is_node
        )}'

    def __repr__(self):
        return f'{type(self).__name__}({', '.join(f'{name}={value}' for name, value in self.__dict__.items())})'


class Block(Node):
    def __init__(self, nodes: tuple[Node, ...]):
        self.nodes = nodes


class _Undetermined(Node):
    def __repr__(self):
        return 'undetermined'


undetermined = _Undetermined()
