from llvmlite import ir

from . import libc


DEREFERENCE_STRUCT = libc.SIZE_TYPE(1)
INDEX_TYPE = ir.IntType(32)


def size_of(builder: ir.IRBuilder, type_: ir.Type):
    """An inline operation returning a label containing the size of a type."""

    offset = builder.gep(type_.as_pointer()('null'), (INDEX_TYPE(1), ))
    return builder.ptrtoint(offset, libc.SIZE_TYPE)
