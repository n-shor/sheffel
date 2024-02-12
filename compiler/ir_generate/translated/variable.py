from __future__ import annotations

from abc import ABCMeta, abstractmethod

from llvmlite import ir, binding

from ...ast.types import VariableType, FunctionType
from ...ast.types.qualifiers import ValueMemoryQualifier, ReferenceMemoryQualifier

from .. import resolve_type, external
from .expression import BaseExpression


class Variable(BaseExpression, metaclass=ABCMeta):
    def __init__(self, type_: VariableType):
        """Constructs the variable and adds an instruction to allocate space for the variable."""
        super().__init__()

        self._type = type_

    @property
    def label(self):
        return self.as_pointer()

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


_REF_COUNTER_TYPE = external.SIZE_TYPE
_STRUCT_INDEX_TYPE = ir.IntType(32)
_DEREFERENCE_STRUCT = external.SIZE_TYPE(1)


class HeapVariable(Variable):
    def __init__(self, builder: ir.IRBuilder, type_: VariableType):

        self._builder = builder

        target_data = binding.create_target_data(self._builder.module.data_layout)

        self._data_type = resolve_type(type_.base_type)
        struct_type = ir.LiteralStructType((_REF_COUNTER_TYPE, self._data_type))

        struct_size = struct_type.get_abi_size(target_data)

        self._generic_ptr = external.malloc(self._builder, external.SIZE_TYPE(struct_size))
        self._struct_ptr = self._builder.bitcast(self._generic_ptr, struct_type.as_pointer())

        self._set_ref_count_to_1()

        super().__init__(type_)

    def as_pointer(self):
        self._builder.load(self._struct_ptr)
        return self._builder.gep(self._struct_ptr, (_DEREFERENCE_STRUCT, _STRUCT_INDEX_TYPE(1),))

    def load(self):
        return self._builder.load(self.as_pointer())

    def assign(self, value):
        raise self._builder.store(value, self.as_pointer())

    # reference counting

    def _get_ref_count_ptr(self):
        self._builder.load(self._struct_ptr)
        return self._builder.gep(self._struct_ptr, (_DEREFERENCE_STRUCT, _STRUCT_INDEX_TYPE(0)))

    def _set_ref_count_to_1(self):
        rfp = self._get_ref_count_ptr()
        self._builder.store(rfp, _REF_COUNTER_TYPE(1))

    def _inc_ref_count(self):
        rfp = self._get_ref_count_ptr()
        loaded = self._builder.load(rfp)
        updated = self._builder.add(loaded, _REF_COUNTER_TYPE(1))
        self._builder.store(updated, rfp)

    def _dec_ref_count(self):
        rfp = self._get_ref_count_ptr()
        loaded = self._builder.load(rfp)
        updated = self._builder.sub(loaded, _REF_COUNTER_TYPE(1))
        is_zero = self._builder.icmp_unsigned('==', updated, _REF_COUNTER_TYPE(0))

        with self._builder.if_else(is_zero) as (then_block, otherwise_block):
            with then_block:
                self.free()

            with otherwise_block:
                self._builder.store(updated, rfp)

    def assign_view(self, assignee: HeapVariable):

        self._dec_ref_count()
        assignee._inc_ref_count()

        assignee_struct = self._builder.gep(assignee._struct_ptr, (_DEREFERENCE_STRUCT,))
        return self._builder.store(assignee_struct, self._struct_ptr)

    def free(self):
        return external.free(self._builder, self._generic_ptr)
