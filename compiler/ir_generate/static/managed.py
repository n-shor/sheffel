from llvmlite import ir

from .static_function import InternalFunction
from . import libc, utils


REF_COUNTER_TYPE = libc.SIZE_TYPE
REF_COUNTER_INDICES = (utils.DEREFERENCE_STRUCT, utils.INDEX_TYPE(0))
DATA_INDICES = (utils.DEREFERENCE_STRUCT, utils.INDEX_TYPE(1))


def _cast_to_generic_struct(builder: ir.IRBuilder, ptr: ir.Value):
    struct_type = ir.LiteralStructType((REF_COUNTER_TYPE, libc.GENERIC_PTR_TYPE.pointee)).as_pointer()
    return builder.bitcast(ptr, struct_type)


def _calculate_total_size(builder: ir.IRBuilder, size: ir.Value):
    return builder.add(size, utils.size_of(builder, libc.SIZE_TYPE))


@InternalFunction.create(ir.FunctionType(libc.GENERIC_PTR_TYPE, (libc.SIZE_TYPE,)))
def new(builder: ir.IRBuilder, size: ir.Value):
    """(data_size: i64) -> managed_object_ptr: i8*
    Allocates a new managed object on the heap, sets its reference count to 1, and returns a pointer to it.
    """
    generic_ptr = libc.malloc(builder, _calculate_total_size(builder, size))

    struct_ptr = _cast_to_generic_struct(builder, generic_ptr)
    builder.load(struct_ptr)
    builder.store(REF_COUNTER_TYPE(1), builder.gep(struct_ptr, REF_COUNTER_INDICES))

    builder.ret(generic_ptr)


@InternalFunction.create(ir.FunctionType(ir.VoidType(), (libc.GENERIC_PTR_TYPE, )))
def add_ref(builder: ir.IRBuilder, ptr: ir.Value):
    """(managed_object_ptr: i8*) -> : void
    Increments the reference count of a managed object.
    """

    struct_ptr = _cast_to_generic_struct(builder, ptr)
    builder.load(struct_ptr)
    ref_count_ptr = builder.gep(struct_ptr, REF_COUNTER_INDICES)
    value = builder.load(ref_count_ptr)
    updated = builder.add(value, REF_COUNTER_TYPE(1))
    builder.store(updated, ref_count_ptr)

    builder.ret_void()


@InternalFunction.create(ir.FunctionType(ir.VoidType(), (libc.GENERIC_PTR_TYPE, )))
def remove_ref(builder: ir.IRBuilder, ptr: ir.Value):
    """(managed_object_ptr: i8*) -> : void
    Decrements the reference count of a managed object.
    If the reference count reaches zero, the object is deleted.
    """
    struct_ptr = _cast_to_generic_struct(builder, ptr)
    builder.load(struct_ptr)
    ref_count_ptr = builder.gep(struct_ptr, REF_COUNTER_INDICES)
    value = builder.load(ref_count_ptr)
    updated = builder.sub(value, REF_COUNTER_TYPE(1))
    is_zero = builder.icmp_unsigned('==', updated, REF_COUNTER_TYPE(0))

    with builder.if_else(is_zero) as (then_block, otherwise_block):
        with then_block:
            libc.free(builder, ptr)

        with otherwise_block:
            builder.store(updated, ref_count_ptr)

    builder.ret_void()


@InternalFunction.create(ir.FunctionType(libc.GENERIC_PTR_TYPE, (libc.GENERIC_PTR_TYPE, )))
def get(builder: ir.IRBuilder, ptr: ir.Value):
    """(managed_object_ptr: i8*) -> data_ptr: i8*
    Gets the pointer to the data of a managed object.
    """
    typed_ptr = _cast_to_generic_struct(builder, ptr)
    builder.load(typed_ptr)
    builder.ret(builder.gep(typed_ptr, DATA_INDICES))


def add_all_to(module: ir.Module):
    new.add_to(module)
    add_ref.add_to(module)
    remove_ref.add_to(module)
    get.add_to(module)
