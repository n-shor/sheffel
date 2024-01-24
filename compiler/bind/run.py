from llvmlite.ir import Module
from llvmlite import binding

from ctypes import CFUNCTYPE, c_int32

from .make import compile_ir, create_execution_engine


def run(ir: Module) -> int:
    """Runs an ir module and returns its main function's output."""

    # All these initializations are required for code generation!
    binding.initialize()
    binding.initialize_native_target()
    binding.initialize_native_asmprinter()  # yes, even this one

    engine = create_execution_engine()
    mod = compile_ir(engine, str(ir))

    # Look up the function pointer (a Python int)
    func_ptr = engine.get_function_address("main")

    # Run the function via ctypes
    cfunc = CFUNCTYPE(c_int32)(func_ptr)
    res = cfunc()

    return res
