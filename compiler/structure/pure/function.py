from . import Node, Block, Memory, Qualified, Type, eval_type_type, Literal, Declaration, array_type
from .utils import make_declarations_block


class _FunctionType(Type):
    def __init__(self):
        super().__init__(
            eval_type_type,
            make_declarations_block(
                argument_types=Qualified(array_type, Memory.EVAL),
                return_type=eval_type_type
            )
        )


function_type = _FunctionType()


class FunctionLiteral(Literal):
    def __init__(self, arguments: tuple[Declaration, ...], return_type: Qualified, body: Block):
        super().__init__(function_type, NotImplemented())  # should become this function literal's ir label

        self.argument_types = tuple(arg.qualified for arg in arguments)
        self.return_type = return_type

        self.arguments = arguments
        self.body = body
