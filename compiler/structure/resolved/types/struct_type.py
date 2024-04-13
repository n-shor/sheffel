from __future__ import annotations

from llvmlite import ir

from ...ir_utils import SIZE_TYPE, INDEX_TYPE
from .. import UnresolvedOperatorError, Type, Variable
from ..values import EvalValue, WeakRefValue
from . import type_type


class StructType(Type):
    """Represents a type with only fields."""

    def __init__(self, fields: tuple[tuple[str, Type], ...], name_hint=''):
        super().__init__(
            type_type,
            ir.LiteralStructType(tuple(type_.ir_type for name, type_ in fields)),
            name_hint
        )

        self.fields = {name: (type_, index) for index, (name, type_) in enumerate(fields)}

    def operator(self, builder, operation, operands):
        if operation != '.':
            return super().operator(builder, operation, operands)

        instance_variable, field_name_value = operands

        if not isinstance(instance_variable, Variable):
            raise UnresolvedOperatorError(f'The left operand of operator {repr(operation)} must be a variable.')

        if not isinstance(field_name_value, EvalValue):
            raise UnresolvedOperatorError(f'The right operand of operator {repr(operation)} must be a literal.')

        field_name = field_name_value.py_value

        if not isinstance(field_name, str):
            raise UnresolvedOperatorError(f'The right operand of operator {repr(operation)} must be a string.')

        instance_ptr = instance_variable.ptr(builder)

        field_type, field_index = self.fields[field_name]
        ptr = builder.gep(instance_ptr, (SIZE_TYPE(1), INDEX_TYPE(field_index)), name=f'{self.name_hint}.{field_name}')
        return WeakRefValue(field_type, ptr)
