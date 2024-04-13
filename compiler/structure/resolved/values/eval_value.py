from llvmlite import ir

from .. import CompilationError, Value, Type


class EvalValue(Value):
    """A compile time constant value, which is inlined, and has no label."""

    def __init__(self, type_: Type, py_value, ir_value: ir.Constant):
        super().__init__(type_)
        self.py_value = py_value
        self._ir_value = ir_value

    def load(self, builder):
        return self._ir_value

    def ptr(self, builder):
        raise CompilationError('Eval value does not have a pointer.')
