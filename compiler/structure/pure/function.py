from . import Node, Block, Memory, Value, Qualified, Type, eval_type_type, array_type
from .utils import make_declarations_block


class _FunctionType(Type):
    def __init__(self):
        super().__init__(
            eval_type_type,
            make_declarations_block(
                return_type=eval_type_type,
                argument_types=Qualified(array_type, Memory.EVAL)
            )
        )


function_type = _FunctionType()


class Function(Value):
    def __init__(self, return_type: Value, argument_types: tuple[Node, ...], body: Block):
        super().__init__(Qualified(function_type, Memory.COPY))
        self.return_type = return_type
        self.argument_types = argument_types
        self.body = body

# Should add "non-eval" function
