from llvmlite import ir

from .. import VariableOperationError, Variable, Type


class WeakRefVariable(Variable):
    """Represents a non-owning reference to another variable."""

    def __init__(self, type_: Type, ptr: ir.NamedValue, name_hint=''):
        super().__init__(type_, name_hint)
        self._ptr = ptr

    def declare(self, builder):
        raise VariableOperationError(f"Weak ref variable {self.name_hint} cannot be declared.")

    def get_ptr(self, builder):
        return self._ptr

    def load(self, builder):
        return builder.load(self._ptr)

    def store(self, builder, value):
        builder.store(value, self._ptr)
