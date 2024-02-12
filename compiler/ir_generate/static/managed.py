from llvmlite import ir

from .. import utils
from .static_function import InternalFunction
from . import libc

DEREFERENCE_STRUCT = libc.SIZE_TYPE(1)
STRUCT_INDEX_TYPE = ir.IntType(32)

_REF_COUNTER_TYPE = libc.SIZE_TYPE


def _cast_to_generic_struct(builder: ir.IRBuilder, ptr: ir.Value):
    struct_type = ir.LiteralStructType((_REF_COUNTER_TYPE, libc.GENERIC_PTR_TYPE.pointee)).as_pointer()
    return builder.bitcast(ptr, struct_type)


def _get_ref_count_ptr(builder: ir.IRBuilder, typed_ptr: ir.Value):
    return builder.gep(typed_ptr, (DEREFERENCE_STRUCT, STRUCT_INDEX_TYPE(0)))


@InternalFunction.create(ir.FunctionType(libc.GENERIC_PTR_TYPE, (libc.SIZE_TYPE,)))
def new(builder: ir.IRBuilder, size: ir.Value):
    """(object_size: i64) -> managed_object_ptr: i8*
    Allocates a new managed object on the heap, sets its reference count to 1, and returns a pointer to it.
    """
    struct_size = builder.add(size, utils.sizeof(_REF_COUNTER_TYPE, as_type=libc.SIZE_TYPE))
    struct_ptr = libc.malloc(builder, struct_size)

    typed_ptr = _cast_to_generic_struct(builder, struct_ptr)
    builder.load(typed_ptr)
    builder.store(_REF_COUNTER_TYPE(1), _get_ref_count_ptr(builder, typed_ptr))
    return typed_ptr


@InternalFunction.create(ir.FunctionType(ir.VoidType(), (libc.GENERIC_PTR_TYPE, )))
def add_ref(builder: ir.IRBuilder, ptr: ir.Value):
    """(managed_object_ptr: i8*) -> : void
    Increments the reference count of a managed object.
    """
    typed_ptr = _cast_to_generic_struct(builder, ptr)
    builder.load(typed_ptr)
    ref_count_ptr = _get_ref_count_ptr(builder, typed_ptr)
    value = builder.load(ref_count_ptr)
    updated = builder.add(value, _REF_COUNTER_TYPE(1))
    builder.store(updated, ref_count_ptr)


@InternalFunction.create(ir.FunctionType(ir.VoidType(), (libc.GENERIC_PTR_TYPE, )))
def remove_ref(builder: ir.IRBuilder, ptr: ir.Value):
    """(managed_object_ptr: i8*) -> : void
    Decrements the reference count of a managed object.
    If the reference count reaches zero, the object is deleted.
    """
    typed_ptr = _cast_to_generic_struct(builder, ptr)
    builder.load(typed_ptr)
    ref_count_ptr = _get_ref_count_ptr(builder, typed_ptr)
    value = builder.load(ref_count_ptr)
    updated = builder.sub(value, _REF_COUNTER_TYPE(1))
    is_zero = builder.icmp_unsigned('==', updated, _REF_COUNTER_TYPE(0))

    with builder.if_else(is_zero) as (then_block, otherwise_block):
        with then_block:
            libc.free(builder, ptr)

        with otherwise_block:
            builder.store(updated, ref_count_ptr)


@InternalFunction.create(ir.FunctionType(libc.GENERIC_PTR_TYPE, (libc.GENERIC_PTR_TYPE, )))
def get_data_ptr(builder: ir.IRBuilder, ptr: ir.Value):
    """(managed_object_ptr: i8*) -> data_ptr: i8*
    Gets the pointer to the data of a managed object.
    """
    typed_ptr = _cast_to_generic_struct(builder, ptr)
    builder.load(typed_ptr)
    return builder.gep(typed_ptr, (DEREFERENCE_STRUCT, STRUCT_INDEX_TYPE(1)))


def add_all_to(module: ir.Module):
    new.add_to(module)
    add_ref.add_to(module)
    remove_ref.add_to(module)
    get_data_ptr.add_to(module)


def get_full_struct_type(data_type: ir.Type):
    return ir.LiteralStructType((_REF_COUNTER_TYPE, data_type))


