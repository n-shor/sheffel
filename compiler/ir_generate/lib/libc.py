from llvmlite import ir

from .static_module import ExternalModule


SIZE_TYPE = ir.IntType(64)
GENERIC_PTR_TYPE = ir.IntType(8).as_pointer()


heap = ExternalModule('libc.heap')

malloc = heap.function(ir.FunctionType(GENERIC_PTR_TYPE, (SIZE_TYPE,))).declare('malloc')
"""(bytes: i64) -> ptr: i8*"""

free = heap.function(ir.FunctionType(ir.VoidType(), (GENERIC_PTR_TYPE,))).declare('free')
"""(ptr: i8*) -> : void"""


utils = ExternalModule('libc.utils')

printf = utils.function(ir.FunctionType(ir.IntType(32), (GENERIC_PTR_TYPE, ), var_arg=True)).declare('printf')
"""(format: i8*, ...) -> printed_count: i32"""

# memory_copy = module.function(ir.FunctionType(ir.VoidType(), (GENERIC_PTR_TYPE, GENERIC_PTR_TYPE, SIZE_TYPE))).declare('memcpy')
# """(dst: i8*, src: i8*, bytes: i64) -> : void"""
