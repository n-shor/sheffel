from llvmlite import ir

ENTRY_LABEL_NAME = 'main'
ENTRY_LABEL_FUNC_TYPE = ir.FunctionType(ir.IntType(32), ())
