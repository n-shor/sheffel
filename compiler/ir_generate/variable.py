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
        self.ptr = builder.alloca(resolve_type(type_))
        self.builder = builder

    def load(self):
        return self.builder.load(self.ptr)

    def as_pointer(self):
        return self.ptr

    def free(self):
        pass


class Parameter(Variable):
    def __init__(self, argument: ir.Argument, type_: VariableType):
        super().__init__(type_)
        self.label = argument

    def load(self):
        return self.label

    def as_pointer(self):
        raise TypeError("Cannot write to a function's parameter.")

    def free(self):
        pass


class HeapVariable(Variable):
    def __init__(self, builder: ir.IRBuilder, type_: VariableType):
        super().__init__(type_)
        size = resolve_type(type_).get_abi_size(binding.create_target_data(builder.module.data_layout))
        self.ptr = malloc_instruction(builder, ir.IntType(64)(size))
        self.builder = builder

    def load(self):
        return self.builder.load(self.ptr)

    def as_pointer(self):
        return self.ptr

    def free(self):
        return free_instruction(self.builder, self.ptr)
