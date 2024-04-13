from llvmlite import ir

from .. import Variable, Type, Value
from ..values import WeakRefValue


class CopyVariable(Variable, WeakRefValue):
    """Represents a variable kept on the stack, which is always copied between uses."""

    def __init__(self, type_: Type, name_hint=''):
        Variable.__init__(self, type_, name_hint)
        WeakRefValue.__init__(self, type_, None)

    def declare(self, builder):
        self._ptr = builder.alloca(self.type_.ir_type, name=self.name_hint)

    def copy_from(self, builder, other):
        return WeakRefValue.copy_from(self, builder, other)
