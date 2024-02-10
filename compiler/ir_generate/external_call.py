from llvmlite import ir


def _get_external_function(builder: ir.IRBuilder, function_name: str):
    return builder.module.globals[function_name]


def malloc_instruction(builder: ir.IRBuilder, size):
    return builder.call(_get_external_function(builder, 'malloc'), (size, ))


def free_instruction(builder: ir.IRBuilder, ptr):
    return builder.call(_get_external_function(builder, 'free'), (ptr, ))
