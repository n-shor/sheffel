from llvmlite import ir

from .static_function import InternalFunction
from . import libc

DEREFERENCE_STRUCT = libc.SIZE_TYPE(1)
INDEX_TYPE = ir.IntType(32)


def size_of(builder: ir.IRBuilder, type_: ir.Type):
    offset = builder.gep(type_.as_pointer()('null'), (INDEX_TYPE(1), ))
    return builder.ptrtoint(offset, libc.SIZE_TYPE)


