from llvmlite import ir

from .. import Type

char_type = Type(ir.IntType(8), 'Char')
string_type = Type(ir.IntType(8).as_pointer(), 'String')
