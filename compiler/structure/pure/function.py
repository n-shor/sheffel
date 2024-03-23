from . import Type, type_type, array_type
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


function_type = _FunctionType()
