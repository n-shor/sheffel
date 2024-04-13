from llvmlite import ir

from .. import Value, Type


class WeakRefValue(Value):
    """A weak reference to a value, which can be edited and read as long as the original value is still in scope."""

    def __init__(self, type_: Type, ptr: ir.NamedValue):
        super().__init__(type_)
        self._ptr = ptr

    def load(self, builder):
        return builder.load(self._ptr)

    def ptr(self, builder):
        return self._ptr
