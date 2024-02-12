from llvmlite import ir

from .static_function import ExternalFunction

SIZE_TYPE = ir.IntType(64)
GENERIC_PTR_TYPE = ir.IntType(8).as_pointer()


malloc = ExternalFunction('malloc', ir.FunctionType(GENERIC_PTR_TYPE, (SIZE_TYPE, )))
"""(bytes: i64) -> ptr: i8*"""

free = ExternalFunction('free', ir.FunctionType(ir.VoidType(), (GENERIC_PTR_TYPE, )))
"""(ptr: i8*) -> : void"""

memory_copy = ExternalFunction('memcpy', ir.FunctionType(ir.VoidType(), (GENERIC_PTR_TYPE, GENERIC_PTR_TYPE, SIZE_TYPE)))
"""(dst: i8*, src: i8*, bytes: i64) -> : void"""


def add_all_to(module: ir.Module):
    malloc.add_to(module)
    free.add_to(module)
    memory_copy.add_to(module)
