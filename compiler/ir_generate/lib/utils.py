from llvmlite import ir

from . import libc


DEREFERENCE_STRUCT = libc.SIZE_TYPE(1)
INDEX_TYPE = ir.IntType(32)


def size_of(builder: ir.IRBuilder, type_: ir.Type):
    """An inline operation returning a label containing the size of a type."""

    offset = builder.gep(type_.as_pointer()('null'), (INDEX_TYPE(1), ))
    return builder.ptrtoint(offset, libc.SIZE_TYPE)


def string_literal(builder: ir.IRBuilder, value: str):
    """Adds a string literal to the module and returns its address."""

    value += '\0'
    bytes_ = bytearray(value.encode())

    type_ = ir.ArrayType(ir.IntType(8), len(bytes_))

    var = ir.GlobalVariable(builder.module, type_, builder.module.get_unique_name())

    var.global_constant = True
    var.initializer = type_(bytes_)

    return builder.gep(var, (INDEX_TYPE(0), INDEX_TYPE(0)))
