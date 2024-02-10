from llvmlite import ir


class ExternalFunction:
    def __init__(self, name: str, type_: ir.FunctionType):
        self.name = name
        self.type_ = type_

    def add(self, module: ir.Module):
        """Adds the external function to the module."""
        ir.Function(module, self.type_, self.name)

    def __call__(self, builder: ir.IRBuilder, *args: ir.Value):
        """Calls the external function"""
        return builder.call(builder.module.globals[self.name], tuple(args))


SIZE_TYPE = ir.IntType(64)
GENERIC_PTR_TYPE = ir.IntType(8).as_pointer()


malloc = ExternalFunction('malloc', ir.FunctionType(GENERIC_PTR_TYPE, (SIZE_TYPE, )))
free = ExternalFunction('free', ir.FunctionType(ir.VoidType(), (GENERIC_PTR_TYPE, )))
