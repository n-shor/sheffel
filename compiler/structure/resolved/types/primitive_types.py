from typing import Callable
import functools as ft

from llvmlite import ir

from .. import UnresolvedOperatorError, Value, Type


int_type, double_type, bool_type, char_type, string_type = (Type(ir.VoidType()), ) * 5
# forward declaration


def _cast_to(builder: ir.IRBuilder, value: ir.NamedValue | ir.Constant, type_: ir.Type) -> ir.NamedValue:
    match value.type, type_:

        case type_from, type_to if type_from == type_to:
            return value

        case ir.IntType(), ir.FloatType() | ir.DoubleType():
            return builder.uitofp(value, type_)

        case ir.FloatType() | ir.DoubleType(), ir.IntType():
            return builder.fptoui(value, type_)

        case ir.IntType(size_from), ir.IntType(size_to) if size_from < size_to:
            return builder.zext(value, type_)

        case ir.IntType(size_from), ir.IntType(size_to) if size_from > size_to:
            return builder.trunc(value, type_)

        case ir.FloatType(), ir.DoubleType():
            return builder.fpext(value, type_)

        case ir.DoubleType(), ir.FloatType():
            return builder.fptrunc(value, type_)

    raise NotImplementedError('Impossible case.')


def _type_precedence(type_: Type, *, _type_hierarchy=(double_type, int_type)):
    return _type_hierarchy.index(type_)


def _arithmetic_op(builder: ir.IRBuilder, operands: tuple[Value, ...], max_type: Type,
                   int_op: Callable, float_op: Callable) -> ir.Instruction:
    """Casts the operands up to the type of the largest present operand, unless it is larger than `max_type`.
    Calls `int_op` if the largest type is an int type, else `float_op` is called.
    """
    largest_operand_type = sorted((operand.type_ for operand in operands), key=_type_precedence)[0]

    if _type_precedence(largest_operand_type) > _type_precedence(max_type):
        raise TypeError(f"An operand is too large for this operation.")

    cast_operands = tuple(_cast_to(builder, operand.load(builder), largest_operand_type) for operand in operands)

    match largest_operand_type:
        case ir.IntType():
            return int_op(*cast_operands)

        case ir.FloatType() | ir.DoubleType():
            return float_op(*cast_operands)

    raise NotImplementedError('Impossible case.')


class _PrimitiveArithmeticType(Type):
    def __init__(self, ir_type: ir.Type, name: str):
        super().__init__(ir_type, name)

    def operator(self, builder, operation, operands):
        try:
            arithmetic_op = ft.partial(_arithmetic_op, builder, operands, self)

            match operation:
                case '+':
                    return arithmetic_op(builder.add, builder.fadd)

                case '-':
                    return arithmetic_op(builder.sub, builder.fsub)

                case '*':
                    return arithmetic_op(builder.mul, builder.fmul)

                case '/':
                    return arithmetic_op(builder.udiv, builder.fdiv)

                case '%':
                    return arithmetic_op(builder.urem, builder.frem)

        except TypeError:
            raise UnresolvedOperatorError(f'Operation {operation} could not be resolved for the given operands: {operands}.')

        return super().operator(builder, operation, operands)


int_type = _PrimitiveArithmeticType(ir.IntType(32), 'Int')
double_type = _PrimitiveArithmeticType(ir.DoubleType(), 'Double')
bool_type = Type(ir.IntType(1), 'Bool')
char_type = Type(ir.IntType(8), 'Char')
string_type = Type(ir.IntType(8).as_pointer(), 'String')
