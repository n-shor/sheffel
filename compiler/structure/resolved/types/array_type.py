from llvmlite import ir

from ...ir_utils import SIZE_TYPE

from .. import UnresolvedOperatorError, Type, Value, Variable
from ..values import EvalValue, WeakRefValue
from . import type_type, int_type, string_type


class ArrayType(Type):
    def __init__(self, element_type: Type, count: int):

        super().__init__(type_type, ir.ArrayType(element_type.ir_type, count),
                         f'ArrayType<count={count}, type={element_type.get_name()}>')
        self.element_type = element_type
        self.count = EvalValue(int_type, count, int_type(count))

    def operator(self, builder, operation, operands):

        match operation, operands:
            case '.', [Value(type_=type_), EvalValue(py_value=field_name)] if type_ is self:
                match field_name:
                    case 'count':
                        return self.count.load(builder)

                    case 'element_type':
                        return self.element_type.load(builder)

                    case _:
                        raise UnresolvedOperatorError(f'{field_name} is not a field of an array.')

            case '[]', [Variable(type_=array_type) as instance, Value(type_=indexer_type) as indexer] if array_type is self:
                if indexer_type is not int_type:
                    raise UnresolvedOperatorError(f'Cannot index an array with the non-integer type {indexer_type}.')

                instance_ptr = instance.get_ptr(builder)
                index = indexer.load(builder)
                element_ptr = builder.gep(instance_ptr, (index,))

                return WeakRefValue(self.element_type, element_ptr)

    def set_all_values(self, builder: ir.IRBuilder, instance: Variable, values: tuple[Value, ...]):
        instance_ptr = instance.ptr(builder)
        for i, value in enumerate(values):
            element_ptr = builder.gep(instance_ptr, (SIZE_TYPE(i),))
            builder.store(value.load(builder), element_ptr)
