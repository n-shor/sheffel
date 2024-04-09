from llvmlite import ir

from .. import Type
from . import type_type


bool_type = Type(type_type, ir.IntType(1), 'Bool')
