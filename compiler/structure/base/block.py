from . import Node


def block(t: type[Node]):
    """Creates a block class for a specific node subclass."""

    class _Block(t):
        def __init__(self, nodes: tuple[t, ...]):
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

    return _Block
