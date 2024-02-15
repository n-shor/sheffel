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


def _increment_ref_count(builder: ir.IRBuilder, ptr: ir.Value):
    """Increments the ref count and returns its value."""

    struct_ptr = _cast_to_generic_struct(builder, ptr)
    builder.load(struct_ptr)
    ref_count_ptr = builder.gep(struct_ptr, REF_COUNTER_INDICES)
    value = builder.load(ref_count_ptr)
    updated = builder.add(value, REF_COUNTER_TYPE(1))
    builder.store(updated, ref_count_ptr)

    return updated


@InternalFunction.create(ir.FunctionType(ir.VoidType(), (libc.GENERIC_PTR_TYPE, )))
def add_ref(builder: ir.IRBuilder, ptr: ir.Value):
    """(managed_object_ptr: i8*) -> : void
    Increments the reference count of a managed object.
    """
    _increment_ref_count(builder, ptr)
    builder.ret_void()


def _decrement_ref_count(builder: ir.IRBuilder, ptr: ir.Value):
    """Decrements the ref count and returns whether the updated value is zero."""

    struct_ptr = _cast_to_generic_struct(builder, ptr)
    builder.load(struct_ptr)
    ref_count_ptr = builder.gep(struct_ptr, REF_COUNTER_INDICES)
    value = builder.load(ref_count_ptr)
    updated = builder.sub(value, REF_COUNTER_TYPE(1))
    is_zero = builder.icmp_unsigned('==', updated, REF_COUNTER_TYPE(0))
    builder.store(updated, ref_count_ptr)

    return is_zero


def _free_if(builder: ir.IRBuilder, ptr: ir.Value, cond: ir.Value):
    with builder.if_then(cond):
        libc.free(builder, ptr)


@InternalFunction.create(ir.FunctionType(ir.VoidType(), (libc.GENERIC_PTR_TYPE, )))
def remove_ref(builder: ir.IRBuilder, ptr: ir.Value):
    """(managed_object_ptr: i8*) -> : void
    Decrements the reference count of a managed object.
    If the reference count reaches zero, the object is deleted.
    """
    is_zero = _decrement_ref_count(builder, ptr)
    _free_if(builder, ptr, is_zero)
    builder.ret_void()


@InternalFunction.create(ir.FunctionType(ir.VoidType(), (libc.GENERIC_PTR_TYPE, libc.GENERIC_PTR_TYPE, libc.SIZE_TYPE)))
def assign_from(builder: ir.IRBuilder, ptr: ir.Value, ptr_from: ir.Value, size: ir.Value):
    """(managed_object_ptr: i8*, managed_object_ptr_from: i8*, data_size: i64) -> : void
    Decrements the reference count of a managed object.
    Sets the variable holding the pointer to that reference to `from` (and increase its ref count).
    If the reference count reaches zero, the old object is deleted.
    """
    is_zero = _decrement_ref_count(builder, ptr)
    _increment_ref_count(builder, ptr_from)

    libc.memory_copy(builder, ptr, ptr_from, _calculate_total_size(builder, size))

    _free_if(builder, ptr, is_zero)
    builder.ret_void()


@InternalFunction.create(ir.FunctionType(libc.GENERIC_PTR_TYPE, (libc.GENERIC_PTR_TYPE, )))
def get_data_ptr(builder: ir.IRBuilder, ptr: ir.Value):
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
    assign_from.add_to(module)
    get_data_ptr.add_to(module)
