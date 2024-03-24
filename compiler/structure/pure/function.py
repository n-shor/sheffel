from . import Node, Block, Value, Type, type_type, Declaration, array_type
from .utils import make_declarations_block


class _FunctionType(Type):
    def __init__(self):
        super().__init__(
            type_type,
            make_declarations_block(
                return_type=type_type,
                argument_types=array_type
            )
        )

    def __repr__(self):
        return 'function_type'


class FunctionComposition(Node):
    def __init__(self, return_type: Value, arguments: tuple[Declaration, ...], body: Block):
        self.return_type = return_type
        self.arguments = arguments
        self.body = body

    def syntax(self):
        return f'{self.return_type.syntax()}({', '.join(argument.syntax() for argument in self.arguments)}) {self.body.syntax()}'


function_type = _FunctionType()
