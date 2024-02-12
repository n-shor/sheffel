from llvmlite import ir

from .static_function import ExternalFunction

SIZE_TYPE = ir.IntType(64)
GENERIC_PTR_TYPE = ir.IntType(8).as_pointer()


malloc = ExternalFunction('malloc', ir.FunctionType(GENERIC_PTR_TYPE, (SIZE_TYPE, )))
free = ExternalFunction('free', ir.FunctionType(ir.VoidType(), (GENERIC_PTR_TYPE, )))


def add_all_to(module: ir.Module):
    malloc.add_to(module)
    free.add_to(module)
