from llvmlite import ir

from .. import VariableOperationError, Variable, Type
from ..values import EvalValue


class EvalVariable(Variable, EvalValue):
    """Represents an eval variable; i.e. a compile time constant."""

    def __init__(self, type_: Type, name_hint=''):
        Variable.__init__(self, type_, name_hint)
        EvalValue.__init__(self, type_, None, None)

    def declare(self, builder):
        pass

    def copy_from(self, builder, other):
        if not isinstance(other, EvalValue):
            raise VariableOperationError(f'Cannot set the eval variable {self.get_name()} from a non eval value.')

        if self.py_value is not None:
            raise VariableOperationError(f'Cannot set the eval variable {self.get_name()}'
                                         f'as it already contains a value.')

        self._ir_value = other.load(builder)
        self.py_value = other.py_value
