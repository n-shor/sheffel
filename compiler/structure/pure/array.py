from . import Type, type_type, unsigned_int_type
from .utils import make_declarations_block


class _ArrayType(Type):
    def __init__(self):
        super().__init__(
            type_type,
            make_declarations_block(
                element_type=type_type,
                count=unsigned_int_type
            )
        )


array_type = _ArrayType()
