from llvmlite import ir

from .. import Type


class _TypeType(Type):
    def __init__(self):
        super().__init__(self, ir.VoidType(), 'type_type')


type_type = _TypeType()
