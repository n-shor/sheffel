from . import Memory, Value, Qualified, Type, eval_type_type, Literal, unsigned_int_type
from .utils import make_declarations_block


class _ArrayType(Type):
    def __init__(self):
        super().__init__(
            eval_type_type,
            make_declarations_block(
                count=Qualified(unsigned_int_type, Memory.EVAL),
                element_type=eval_type_type
            )
        )


array_type = _ArrayType()


class ArrayLiteral(Literal):
    def __init__(self, values: tuple[Value, ...], element_type: Qualified):
        super().__init__(array_type, NotImplemented())  # should become this array literal's counterpart ir vector

        self.count = len(values)
        self.element_type = element_type

        self.values = values
