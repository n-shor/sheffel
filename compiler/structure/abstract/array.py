from . import Node, Value, Type, type_type, unsigned_int_type
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

    def __repr__(self):
        return 'array_type'


class ArrayComposition(Node):
    def __init__(self, element_type: Value, values: tuple[Value, ...]):
        self.element_type = element_type
        self.values = values

    def syntax(self):
        return f'{self.element_type.syntax()}[{', '.join(value.syntax() for value in self.values)}]'


array_type = _ArrayType()
