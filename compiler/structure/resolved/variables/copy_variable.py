from llvmlite import ir

from .. import VariableOperationError, Variable, Type


class CopyVariable(Variable):
    """Represents a variable kept on the stack, which is always copied between uses."""

    def __init__(self, type_: Type, name_hint=''):
        super().__init__(type_, name_hint)
        self._ptr: ir.NamedValue = None
        self._has_value = False

    def declare(self, builder):
        self._ptr = builder.alloca(self.type_.ir_type, name=self.name_hint)

    def get_ptr(self, builder):
        if self._ptr is None:
            raise VariableOperationError(f"Attempted to get the pointer to the undeclared copy variable {self.get_name()}.")

        return self._ptr

    def load(self, builder):
        if self._has_value is False:
            raise VariableOperationError(f"Usage of uninitialized copy variable {self.get_name()}.")

        return builder.load(self._ptr)

    def store(self, builder, value):
        builder.store(value, self._ptr)
        self._has_value = True
