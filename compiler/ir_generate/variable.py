from abc import ABC, abstractmethod

from llvmlite import ir, binding

from ..ast.types import VariableType, FunctionType
from ..ast.types.qualifiers import ValueMemoryQualifier, ReferenceMemoryQualifier
from . import resolve_type, external


class Variable(ABC):
    def __init__(self, type_: VariableType):
        """Constructs the variable and adds an instruction to allocate space for the variable."""
        self._type = type_

    @abstractmethod
    def load(self) -> ir.Instruction:
        """Adds an instruction to load the variable for reading."""

    @abstractmethod
    def as_pointer(self) -> ir.Instruction:
        """Returns the variable as a pointer."""

    @abstractmethod
    def free(self) -> ir.Instruction:
        """Adds an instruction to free space allocated for the variable."""

    def get_type(self):
        return self._type


class StackVariable(Variable):
    def __init__(self, builder: ir.IRBuilder, type_: VariableType):
        super().__init__(type_)
        self._ptr = builder.alloca(resolve_type(type_))
        self._builder = builder

    def load(self):
        return self._builder.load(self._ptr)

    def as_pointer(self):
        return self._ptr

    def free(self):
        pass


class Parameter(Variable):
    def __init__(self, argument: ir.Argument, type_: VariableType):
        super().__init__(type_)
        self._label = argument

    def load(self):
        return self._label

    def as_pointer(self):
        raise TypeError("Cannot write to a function's parameter.")

    def free(self):
        pass


_REF_COUNTER_TYPE = external.SIZE_TYPE
_STRUCT_INDEX_TYPE = ir.IntType(32)
_DEREFERENCE_STRUCT = external.SIZE_TYPE(1)


class HeapVariable(Variable):
    def __init__(self, builder: ir.IRBuilder, type_: VariableType):

        target_data = binding.create_target_data(builder.module.data_layout)

        self._data_type = resolve_type(type_.base_type)
        struct_type = ir.LiteralStructType((_REF_COUNTER_TYPE, self._data_type))

        struct_size = struct_type.get_abi_size(target_data)

        self._generic_ptr = external.malloc(builder, external.SIZE_TYPE(struct_size))
        self._struct_ptr = builder.bitcast(self._generic_ptr, struct_type.as_pointer())

        builder.load(self._struct_ptr)
        ref_counter_ptr = builder.gep(self._struct_ptr, (_DEREFERENCE_STRUCT, _STRUCT_INDEX_TYPE(0)))
        builder.store(_REF_COUNTER_TYPE(1), ref_counter_ptr)  # stores a 1 in the reference_counter

        self._builder = builder

        super().__init__(type_)

    def load(self):
        return self._builder.load(self.as_pointer())

    def as_pointer(self):
        self._builder.load(self._struct_ptr)
        return self._builder.gep(self._struct_ptr, (_DEREFERENCE_STRUCT, _STRUCT_INDEX_TYPE(1),))

    def free(self):
        return external.free(self._builder, self._generic_ptr)


def create_variable(builder: ir.IRBuilder, type_: VariableType) -> Variable:
    match type_:
        case VariableType(memory=ValueMemoryQualifier()):
            return StackVariable(builder, type_)

        case VariableType(base_type=FunctionType()):
            return StackVariable(builder, type_)

        case VariableType(memory=ReferenceMemoryQualifier()):
            return HeapVariable(builder, type_)

        case _:
            raise TypeError("Unknown variable type.")
