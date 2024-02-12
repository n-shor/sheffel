from __future__ import annotations

from abc import ABCMeta, abstractmethod

from llvmlite import ir

from ...ast.types import VariableType, FunctionType
from ...ast.types.qualifiers import ValueMemoryQualifier, ReferenceMemoryQualifier

from .. import resolve_type
from .. import utils
from ..static import managed, libc

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
        self._ptr = managed.new(builder, utils.sizeof(self._data_type, as_type=libc.SIZE_TYPE))

        super().__init__(type_)

    def as_pointer(self):
        generic_ptr = managed.get_data_ptr(self._builder, self._ptr)
        return self._builder.bitcast(generic_ptr, self._data_type.as_pointer())

    def load(self):
        return self._builder.load(self.as_pointer())

    def assign(self, value):
        return self._builder.store(value, self.as_pointer())

    def _get_typed_struct_ptr(self):
        struct_type = ir.LiteralStructType((managed.REF_COUNTER_TYPE, self._data_type)).as_pointer()
        return self._builder.bitcast(self._ptr, struct_type)

    def _get_sub_ptrs(self):
        struct_ptr = self._get_typed_struct_ptr()
        return (
            self._builder.gep(struct_ptr, managed.REF_COUNTER_INDICES),
            self._builder.gep(struct_ptr, managed.DATA_INDICES)
        )

    def assign_view(self, assignee: HeapVariable):

        managed.remove_ref(self._builder, self._ptr)
        managed.add_ref(self._builder, assignee._ptr)

        self_ref_counter, self_data = self._get_sub_ptrs()
        assignee_ref_counter, assignee_data = assignee._get_sub_ptrs()

        self._builder.store(self._builder.load(assignee_ref_counter), self_ref_counter)
        return self._builder.store(self._builder.load(assignee_data), self_data)

    def free(self):
        managed.remove_ref(self._builder, self._ptr)
