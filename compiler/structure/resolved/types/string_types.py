from llvmlite import ir

from .. import Type
from . import type_type

char_type = Type(type_type, ir.IntType(8), 'Char')
string_type = Type(type_type, ir.IntType(8).as_pointer(), 'String')
