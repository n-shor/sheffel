from llvmlite import ir

from .. import Type


int_type = Type(ir.IntType(32), 'Int')
double_type = Type(ir.DoubleType(), 'Double')
bool_type = Type(ir.IntType(1), 'Bool')
char_type = Type(ir.IntType(8), 'Char')
string_type = Type(ir.IntType(8).as_pointer(), 'String')
