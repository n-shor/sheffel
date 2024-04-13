from llvmlite import ir

from .. import ValueOperationError, Value, Type


class WeakRefValue(Value):
    """A weak reference to a value, which can be edited and read as long as the original value is still in scope."""

    def __init__(self, type_: Type, ptr: ir.NamedValue):
        super().__init__(type_)
        self._ptr = ptr
        self._has_value = False

    def ptr(self, builder):
        return self._ptr

    def load(self, builder):
        if not self._has_value:
            raise ValueOperationError("Cannot load a weak reference with no value.")

        return builder.load(self._ptr)

    def copy_from(self, builder: ir.IRBuilder, other: Value):
        builder.store(other.load(builder), self._ptr)
        self._has_value = True
