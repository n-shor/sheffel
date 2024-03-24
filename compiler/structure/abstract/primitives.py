from llvmlite import ir

from . import Block, Type, type_type, Literal


class _PrimitiveTypeType(Type):
    def __init__(self):
        super().__init__(type_type, Block(()))  # missing an instance operator?


primitive_type_type = _PrimitiveTypeType()


class _PrimitiveTypeBase(Type):
    """Base class for primitive type definitions."""

    def __init__(self, ir_type: ir.Type):
        super().__init__(primitive_type_type, Block(()))
        self.ir_type = ir_type

    def make_literal(self, value):
        return Literal(self, self.ir_type(value))


class _UnsignedIntType(_PrimitiveTypeBase):
    def __init__(self):
        super().__init__(ir.IntType(32))

    def __repr__(self):
        return 'unsigned_int_type'


class _DoubleType(_PrimitiveTypeBase):
    def __init__(self):
        super().__init__(ir.DoubleType())

    def __repr__(self):
        return 'double_type'


unsigned_int_type = _UnsignedIntType()
double_type = _DoubleType()
