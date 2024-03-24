from llvmlite import ir

from . import Value, Type


class Literal(Value):
    def __init__(self, type_: Type, value: ir.Value):
        super().__init__(type_)
        self.value = value

    def syntax(self):
        return f'L<({self.value}):{self.type_.syntax()}>'
