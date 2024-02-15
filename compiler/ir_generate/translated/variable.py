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

    @property
    def label(self):
        return self.load()

    @property
    def type_(self):
        return self._type

    @abstractmethod
    def as_pointer(self) -> ir.Instruction:
        """Returns the variable as a pointer."""

    @abstractmethod
    def load(self) -> ir.Instruction:
        """Adds an instruction to load the variable for reading."""

    @abstractmethod
    def assign(self, value: ir.Value) -> ir.Instruction:
        """Adds an instruction to assign a value into the variable."""

    @abstractmethod
    def free(self) -> ir.Instruction:
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
    def __init__(self, builder: ir.IRBuilder, type_: VariableType):
        self._ptr = builder.alloca(resolve_type(type_))
        self._builder = builder

        super().__init__(type_)

    def as_pointer(self):
        return self._ptr

    def load(self):
        return self._builder.load(self._ptr)

    def assign(self, value):
        return self._builder.store(value, self._ptr)

    def free(self):
        pass


class Parameter(Variable):
    def __init__(self, argument: ir.Argument, type_: VariableType):
        super().__init__(type_)
        self._label = argument

    def as_pointer(self):
        raise TypeError("Function parameters have no pointers.")

    def load(self):
        return self._label

    def assign(self, value):
        raise TypeError("Cannot write to a function's parameter.")

    def free(self):
        pass


class HeapVariable(Variable):
    def __init__(self, builder: ir.IRBuilder, type_: VariableType):

        self._builder = builder
        self._data_type = resolve_type(type_.base_type)

        self._stack_var = builder.alloca(libc.GENERIC_PTR_TYPE)
        ptr = managed.new(builder, utils.size_of(self._builder, self._data_type))
        builder.store(ptr, self._stack_var)

        super().__init__(type_)

    def _get_generic_ptr(self):
        return self._builder.load(self._stack_var)

    def as_pointer(self):
        data_ptr = managed.get_data_ptr(self._builder, self._get_generic_ptr())
        return self._builder.bitcast(data_ptr, self._data_type.as_pointer())

    def load(self):
        return self._builder.load(self.as_pointer())

    def assign(self, value):
        return self._builder.store(value, self.as_pointer())

    def assign_view(self, assignee: HeapVariable):
        """Assigns the `assignee` to the `assigned`."""

        instruction = managed.assign_from(
            self._builder, self._get_generic_ptr(), assignee._get_generic_ptr(),
            utils.size_of(self._builder, self._data_type)
        )

        self._data_type = assignee._data_type
        self._builder.store(assignee._get_generic_ptr(), self._stack_var)

        return instruction

    def free(self):
        managed.remove_ref(self._builder, self._get_generic_ptr())
