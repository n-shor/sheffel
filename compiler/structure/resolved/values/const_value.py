from llvmlite import ir

from .. import CompilationError, Value, Type


class ConstValue(Value):
    """A value which can only be read."""

    def __init__(self, type_: Type, value: ir.Value):
        super().__init__(type_)
        self._value = value

    def load(self, builder):
        return self._value

    def ptr(self, builder):
        raise CompilationError('Cannot get the pointer of a constant value.')
