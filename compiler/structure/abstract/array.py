from . import Node, Value


class ArrayComposition(Node):
    def __init__(self, element_type: Value, values: tuple[Value, ...]):
        self.element_type = element_type
        self.values = values

    def syntax(self):
        return f'{self.element_type.syntax()}[{', '.join(value.syntax() for value in self.values)}]'
