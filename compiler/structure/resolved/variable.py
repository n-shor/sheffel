from abc import ABCMeta, abstractmethod

from llvmlite import ir

from . import CompilationError, Scoped, Type, Value


class VariableOperationError(CompilationError):
    """An unsupported operation on a variable."""


class Variable(Scoped, Value, metaclass=ABCMeta):
    """Represents a value holding object."""

    def __init__(self, type_: Type, name_hint=''):
        super().__init__(name_hint)
        self.type_ = type_

    @abstractmethod
    def declare(self, builder: ir.IRBuilder) -> None:
        """Adds ir code which declares the variable."""

    @abstractmethod
    def store(self, builder: ir.IRBuilder, value: ir.Value) -> None:
        """Adds ir code which stores data to the variable."""


class EvalVariable(Variable):
    """Represents an eval variable; i.e. a compile time constant."""

    def __init__(self, type_: Type, name_hint=''):
        super().__init__(type_, name_hint)
        self.value: ir.Value | None = None

    def declare(self, builder):
        pass

    def load(self, builder):
        if self.value is None:
            raise VariableOperationError(f'Usage of uninitialized eval variable {self.get_name()}.')

        return self.value

    def store(self, builder, value):
        if self.value is not None:
            raise VariableOperationError(f"Eval variable {self.get_name()}={self.value} cannot be changed.")

        self.value = value


class CopyVariable(Variable):
    """Represents a variable kept on the stack, which is always copied between uses."""

    def __init__(self, type_: Type, name_hint=''):
        super().__init__(type_, name_hint)
        self._ptr: ir.NamedValue = None
        self._has_value = False

    def declare(self, builder):
        self._ptr = builder.alloca(self.type_.ir_type, name=self.name_hint)

    def load(self, builder):
        if self._has_value is False:
            raise VariableOperationError(f"Usage of uninitialized copy variable {self.get_name()}.")

        return builder.load(self._ptr)

    def store(self, builder, value):
        builder.store(value, self._ptr)
        self._has_value = True


class WeakRefVariable(Variable):
    """Represents a non-owning reference to another variable."""

    def __init__(self, type_: Type, ptr: ir.NamedValue, name_hint=''):
        super().__init__(type_, name_hint)
        self._ptr = ptr

    def declare(self, builder):
        raise VariableOperationError(f"Weak ref variable {self.name_hint} cannot be declared.")

    def load(self, builder):
        return builder.load(self._ptr)

    def store(self, builder, value):
        builder.store(value, self._ptr)
