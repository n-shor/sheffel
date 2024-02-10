from abc import ABC, abstractmethod

from llvmlite import ir, binding

from ..ast.types import VariableType
from . import resolve_type
from .external_call import malloc_instruction, free_instruction


class Variable(ABC):
    def __init__(self, type_: VariableType):
        """Constructs the variable and adds an instruction to allocate space for the variable."""
        self.type_ = type_

    @abstractmethod
    def load(self) -> ir.Instruction:
        """Adds an instruction to load the variable for reading."""

    @abstractmethod
    def as_pointer(self) -> ir.Instruction:
        """Returns the variable as a pointer."""

    @abstractmethod
    def free(self) -> ir.Instruction:
        """Adds an instruction to free space allocated for the variable."""


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


_malloc_size_type = ir.IntType(64)
_generic_ptr_type = ir.IntType(8).as_pointer()


class HeapVariable(Variable):
    def __init__(self, builder: ir.IRBuilder, type_: VariableType):
        super().__init__(type_)

        ir_value_type = resolve_type(type_.base_type)
        target_data = binding.create_target_data(builder.module.data_layout)
        size = ir_value_type.get_abi_size(target_data)

        self._generic_ptr = malloc_instruction(builder, _malloc_size_type(size))
        self._ptr = builder.bitcast(self._generic_ptr, ir_value_type.as_pointer())

        self._builder = builder

    def load(self):
        return self._builder.load(self._ptr)

    def as_pointer(self):
        return self._ptr

    def free(self):
        return free_instruction(self._builder, self._generic_ptr)
