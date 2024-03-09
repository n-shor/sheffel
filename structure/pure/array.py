from . import Memory, Value, Type, type_type, unsigned_int_type
from .utils import make_declarations_block


class _ArrayType(Type):
    def __init__(self):
        super().__init__(
            type_type,
            make_declarations_block(
                element_type=(type_type, Memory.EVAL),
                count=(unsigned_int_type, Memory.EVAL)
            )
        )


array_type = _ArrayType()


class Array(Value):
    """Represents a run-time array defined by its count."""

    def __init__(self, element_type: Value, count: Value):
        super().__init__(array_type, Memory.COPY)
        self.element_type = element_type
        self.count = count


class EvaluatedArray(Value):
    """Represents a compile-time array defined with its values."""

    def __init__(self, element_type: Value, values: tuple[Value, ...]):
        super().__init__(array_type, Memory.EVAL)
        self.element_Type = element_type
        self.values = values
