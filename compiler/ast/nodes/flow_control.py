from . import Node


class Block(Node):
    """Represents a block of code made of several lines. This is effectively a scope."""
    def __init__(self, *statements: Node):
        super().__init__()

        self.statements = statements


class FlowControl(Node):
    """Represents any flow control statement."""
    def __init__(self):
        super().__init__()



