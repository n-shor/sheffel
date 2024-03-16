from llvmlite import ir

from . import Block, Memory, Type, Qualified, eval_type_type


class _PrimitiveTypeType(Type):
    def __init__(self):
        super().__init__(eval_type_type, Block(()))


eval_primitive_type_type = Qualified(_PrimitiveTypeType(), Memory.EVAL)


class _PrimitiveTypeBase(Type):  # will not affect the type structure, this is a compiler helper
    def __init__(self, ir_type: ir.Type):
        super().__init__(eval_primitive_type_type, Block(()))
        self.ir_type = ir_type

    def __repr__(self):
        return f'{type(self).__name__}()'


class _UnsignedIntType(_PrimitiveTypeBase):
    def __init__(self):
        super().__init__(ir.IntType(32))


class _DoubleType(_PrimitiveTypeBase):
    def __init__(self):
        super().__init__(ir.DoubleType())


unsigned_int_type = _UnsignedIntType()
double_type = _DoubleType()
