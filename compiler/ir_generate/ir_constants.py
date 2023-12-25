from llvmlite import ir

int32_t = ir.IntType(32)

ENTRY_LABEL_NAME = 'main'
ENTRY_LABEL_FUNC_TYPE = ir.FunctionType(int32_t, ())
