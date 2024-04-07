from .. import base


class Node(base.Node):
    pass


class Block(base.block(Node)):
    pass


class Named(Node):
    def __init__(self, name: str):
        self.name = name

    def syntax(self):
        return f'"{self.name}"'
