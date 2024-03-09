from llvmlite import ir

from . import Block, Type, type_type


class _PrimitiveTypeType(Type):
    def __init__(self):
        super().__init__(type_type, Block(()))


primitive_type_type = _PrimitiveTypeType()  # currently empty


class _PrimitiveTypeBase(Type):  # will not affect the type structure, this is a compiler helper
    def __init__(self, ir_type: ir.Type):
        super().__init__(primitive_type_type, Block(()))
        self.ir_type = ir_type


class _UnsignedIntType(_PrimitiveTypeBase):
    def __init__(self):
        super().__init__(ir.IntType(32))


unsigned_int_type = _UnsignedIntType()
