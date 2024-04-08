class Node:
    def syntax(self):
        """Returns the syntax representation as string."""
        return repr(self)

    def __repr__(self):
        return f'{type(self).__name__}({', '.join(f'{name}={repr(value)}' for name, value in self.__dict__.items())})'


class Block(Node):
    def __init__(self, nodes: tuple[Node, ...]):
        self.nodes = nodes

    def syntax(self):
        with self._BlockText() as block_text:
            block_text.set_lines(tuple(node.syntax() for node in self.nodes))
            return str(block_text)

    class _BlockText:
        _global_indent = 0

        def __init__(self):
            self.indent = None
            self.lines = ()

        def __enter__(self):
            self.indent = type(self)._global_indent
            type(self)._global_indent += 1
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            type(self)._global_indent -= 1

        def set_lines(self, lines: tuple[str, ...]):
            self.lines = lines

        def __str__(self):
            prefix = '\t' * self.indent
            line_prefix = '\n' + '\t' * (self.indent + 1)
            return f'{{{line_prefix}{line_prefix.join(self.lines)}\n{prefix}}}'
