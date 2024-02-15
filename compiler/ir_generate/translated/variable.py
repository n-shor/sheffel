from __future__ import annotations

from abc import ABCMeta, abstractmethod

from llvmlite import ir

from ...ast.types import VariableType, FunctionType
from ...ast.types.qualifiers import ValueMemoryQualifier, ReferenceMemoryQualifier

from .. import resolve_type
from ..static import managed, utils, libc

from .expression import BaseExpression


class Variable(BaseExpression, metaclass=ABCMeta):
    def __init__(self, type_: VariableType):
        """Constructs the variable and adds an instruction to allocate space for the variable."""
        super().__init__()

        self._type = type_

    def label(self, builder):
        return self.load(builder)

    @property
    def type_(self):
        return self._type

    @abstractmethod
    def get_ptr(self, builder: ir.IRBuilder) -> ir.Value:
        """Returns the variable as a pointer."""

    @abstractmethod
    def load(self, builder: ir.IRBuilder) -> ir.Value:
        """Loads the value of the variable."""

    @abstractmethod
    def assign(self, builder: ir.IRBuilder, value: ir.Value) -> ir.Value:
        """Adds an instruction to assign a value into the variable."""

    @abstractmethod
    def free(self, builder: ir.IRBuilder) -> ir.Value:
        """Adds an instruction to free space allocated for the variable."""

    @classmethod
    def create(cls, builder: ir.IRBuilder, type_: VariableType) -> Variable:
        """Creates the correct ir variable based on the variable's type"""

        match type_:
            case VariableType(memory=ValueMemoryQualifier()):
                return StackVariable(builder, type_)

            case VariableType(base_type=FunctionType()):
                return StackVariable(builder, type_)

            case VariableType(memory=ReferenceMemoryQualifier()):
                return HeapVariable(builder, type_)

            case _:
                raise TypeError("Unknown variable type.")


class StackVariable(Variable):
    def __init__(self, builder: ir.IRBuilder, type_: VariableType, ir_type: ir.Type = None):
        self._ptr = builder.alloca(ir_type if ir_type is not None else resolve_type(type_))

        super().__init__(type_)

    def get_ptr(self, builder):
        return self._ptr

    def load(self, builder):
        return builder.load(self._ptr)

    def assign(self, builder, value):
        return builder.store(value, self._ptr)

    def free(self, builder):
        pass


class Parameter(Variable):
    def __init__(self, argument: ir.Argument, type_: VariableType):
        super().__init__(type_)
        self._label = argument

    def get_ptr(self, builder):
        raise TypeError("Function parameters have no pointers.")

    def load(self, builder):
        return self._label

    def assign(self, builder, value):
        raise TypeError("Cannot write to a function's parameter.")

    def free(self, builder):
        pass


class HeapVariable(Variable):
    def __init__(self, builder: ir.IRBuilder, type_: VariableType):
        super().__init__(type_)

        self._data_type = resolve_type(type_.base_type)

        self._ptr_var = StackVariable(builder, type_, libc.GENERIC_PTR_TYPE)
        self._ptr_var.assign(builder, managed.new(builder, utils.size_of(builder, self._data_type)))

    def get_ptr(self, builder):
        data_ptr = managed.get(builder, self._ptr_var.load(builder))
        return builder.bitcast(data_ptr, self._data_type.as_pointer())

    def load(self, builder):
        return builder.load(self.get_ptr(builder))

    def assign(self, builder, value):
        return builder.store(value, self.get_ptr(builder))

    def assign_view(self, builder, assignee: HeapVariable):
        """Assigns the `assignee` to the `assigned`."""

        self._data_type = assignee._data_type

        assignee_ptr = assignee._ptr_var.load(builder)

        managed.remove_ref(builder, self._ptr_var.load(builder))
        managed.add_ref(builder, assignee_ptr)
        return self._ptr_var.assign(builder, assignee_ptr)

    def free(self, builder):
        managed.remove_ref(builder, self._ptr_var.load(builder))
