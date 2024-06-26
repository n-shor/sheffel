from llvmlite import ir

from .static_module import InternalModule
from . import libc, utils


REF_COUNTER_TYPE = libc.SIZE_TYPE
REF_COUNTER_INDICES = (utils.DEREFERENCE_STRUCT, utils.INDEX_TYPE(0))
DATA_INDICES = (utils.DEREFERENCE_STRUCT, utils.INDEX_TYPE(1))


generic = InternalModule('managed.generic')
libc.heap.add_to(generic.module)


def _cast_to_generic_struct(builder: ir.IRBuilder, ptr: ir.Value):
    struct_type = ir.LiteralStructType((REF_COUNTER_TYPE, libc.GENERIC_PTR_TYPE.pointee)).as_pointer()
    return builder.bitcast(ptr, struct_type)


def _calculate_total_size(builder: ir.IRBuilder, size: ir.Value):
    return builder.add(size, utils.size_of(builder, libc.SIZE_TYPE))


@generic.function(ir.FunctionType(libc.GENERIC_PTR_TYPE, (libc.SIZE_TYPE,))).define
def new(builder: ir.IRBuilder, size: ir.Value):
    """(data_size: i64) -> managed_object_ptr: i8*
    Allocates a new managed object on the heap, sets its reference count to 1, and returns a pointer to it.
    """
    generic_ptr = libc.malloc(builder, _calculate_total_size(builder, size))

    struct_ptr = _cast_to_generic_struct(builder, generic_ptr)
    builder.load(struct_ptr)
    builder.store(REF_COUNTER_TYPE(1), builder.gep(struct_ptr, REF_COUNTER_INDICES))

    builder.ret(generic_ptr)


@generic.function(ir.FunctionType(ir.VoidType(), (libc.GENERIC_PTR_TYPE,))).define
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


@generic.function(ir.FunctionType(ir.VoidType(), (libc.GENERIC_PTR_TYPE,))).define
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


@generic.function(ir.FunctionType(ir.VoidType(), (libc.GENERIC_PTR_TYPE.as_pointer(), libc.GENERIC_PTR_TYPE.as_pointer()))).define
def assign_indirect(builder: ir.IRBuilder, ptr_to_a_ptr: ir.Value, ptr_to_v_ptr: ir.Value):
    """(ptr_to_managed_object_ptr: i8**, ptr_to_managed_object_ptr: i8**) -> : void
    Assigns `v` to `a`. Performs necessary incrementing and decrementing."""
    value_ptr = builder.load(ptr_to_v_ptr)
    assigned_ptr = builder.load(ptr_to_a_ptr)

    not_same = builder.icmp_unsigned('!=', value_ptr, assigned_ptr)

    with builder.if_then(not_same):
        remove_ref(builder, assigned_ptr)
        add_ref(builder, value_ptr)
        builder.store(value_ptr, ptr_to_a_ptr)

    builder.ret_void()


@generic.function(ir.FunctionType(libc.GENERIC_PTR_TYPE, (libc.GENERIC_PTR_TYPE,))).define
def get(builder: ir.IRBuilder, ptr: ir.Value):
    """(managed_object_ptr: i8*) -> data_ptr: i8*
    Gets the pointer to the data of a managed object.
    """
    typed_ptr = _cast_to_generic_struct(builder, ptr)
    builder.load(typed_ptr)
    builder.ret(builder.gep(typed_ptr, DATA_INDICES))
