from __future__ import annotations
from abc import ABCMeta, abstractmethod

from llvmlite import ir

from ..ir_utils import SIZE_TYPE, INDEX_TYPE

from . import Scoped


class Type(Scoped, metaclass=ABCMeta):
    def __init__(self, ir_type: ir.Type, name_hint=''):
        super().__init__(name_hint)
        self.ir_type = ir_type

    @abstractmethod
    def access_field(self, builder: ir.IRBuilder, instance_ptr: ir.Value, name: str) -> Variable:
        """Adds proper instructions to return a pointer to a field of a value of this type."""

    # maybe add another access method which returns the non ir type of fields
    # eval field can be kept in the scope with an (owner_name + name) name, since they are resolved in-scope
    # static variables are variables which are both eval and have an initializer


class StructType(Type):
    """Represents a type with only fields."""

    def __init__(self, fields: tuple[tuple[str, Type], ...]):
        self.fields = {name: (type_, index) for index, (name, type_) in enumerate(fields)}
        super().__init__(ir.LiteralStructType(tuple(type_.ir_type for name, type_ in fields)))

    def access_field(self, builder, instance_ptr, name):
        field_type, field_index = self.fields[name]
        ptr = builder.gep(instance_ptr, (SIZE_TYPE(1), INDEX_TYPE(field_index)))
        return WeakRefVariable(field_type, ptr, f'{self.name_hint}.{name}')


from . import Variable, WeakRefVariable
