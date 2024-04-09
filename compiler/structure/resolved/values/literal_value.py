from llvmlite import ir

from .. import Value, Type


class LiteralValue(Value):
    def __init__(self, type_: Type, py_value, ir_value: ir.Constant):
        super().__init__(type_)
        self._py_value = py_value
        self._ir_value = ir_value

    def value(self):
        """Returns the python equivalent to the value."""
        return self._py_value

    def load(self, builder):
        return self._ir_value
