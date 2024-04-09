from llvmlite import ir

from .. import Value, Type


class ResultValue(Value):
    def __init__(self, type_: Type, value: ir.NamedValue):
        super().__init__(type_)
        self._value = value

    def load(self, builder):
        return self._value
