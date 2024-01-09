from .node import Node


class FlowControl(Node):
    """Represents any flow control statement."""
    def __init__(self):
        super().__init__()


class Return(FlowControl):
    """A terminator statement returning another statement."""
    def __init__(self, returnee: Node):
        super().__init__()

        self.returnee = returnee


class Block(Node):
    """Represents a block of code made of several lines."""
    def __init__(self, *statements: Node):
        super().__init__()

        self.statements = statements
