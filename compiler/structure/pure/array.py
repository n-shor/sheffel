from . import Memory, Value, Type, Qualified, eval_type_type, unsigned_int_type
from .utils import make_declarations_block


class _ArrayType(Type):
    def __init__(self):
        super().__init__(
            eval_type_type,
            make_declarations_block(
                element_type=eval_type_type,
                count=Qualified(unsigned_int_type, Memory.EVAL)
            )
        )


array_type = _ArrayType()


class Array(Value):
    def __init__(self, element_type: Value, values: tuple[Value, ...]):
        super().__init__(Qualified(array_type, Memory.COPY))
        self.element_type = element_type
        self.values = values
