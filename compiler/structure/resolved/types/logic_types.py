from llvmlite import ir

from .. import Type


bool_type = Type(ir.IntType(1), 'Bool')
