from . import Node, Block


class FunctionComposition(Node):
    def __init__(self, return_type: Node, arguments: tuple[Node, ...], body: Block):
        self.return_type = return_type
        self.arguments = arguments
        self.body = body

    def syntax(self):
        return f'{self.return_type.syntax()}({', '.join(argument.syntax() for argument in self.arguments)}) {self.body.syntax()}'
