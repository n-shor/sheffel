from llvmlite import ir

from .. import VariableOperationError, Variable, Type


class EvalVariable(Variable):
    """Represents an eval variable; i.e. a compile time constant."""

    def __init__(self, type_: Type, name_hint=''):
        super().__init__(type_, name_hint)
        self._value: ir.Constant | None = None

    def declare(self, builder):
        pass

    def get_ptr(self, builder):
        raise VariableOperationError(f'Cannot get the pointer to an eval variable as it has no storage space.')

    def load(self, builder):
        if self._value is None:
            raise VariableOperationError(f'Usage of uninitialized eval variable {self.get_name()}.')

        return self._value

    def store(self, builder, value):
        if self._value is not None:
            raise VariableOperationError(f"Eval variable {self.get_name()}={self._value} cannot be changed.")

        if not isinstance(value, ir.Constant):
            raise VariableOperationError(f"Eval variable {self.get_name()} set from the non-constant {value}.")

        self._value = value
