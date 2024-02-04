from llvmlite import ir

from .unqualified_type import DirectUnqualifiedType


constant_types: dict[str, ir.Type] = {
    'Int': ir.IntType(32),
    'Long': ir.IntType(64),
    'Float': ir.FloatType(),
    'Double': ir.DoubleType(),
    'String': None,
    'Bool': ir.IntType(1)
}


class LiteralType(DirectUnqualifiedType):
    """The type information of a literal value."""
    def __init__(self, type_: ir.Type):
        super().__init__(type_)

    def __repr__(self):
        return type(self).__name__


class NumericLiteralType(LiteralType):
    """The type information of a numeric literal value."""


class IntegralLiteralType(NumericLiteralType):
    """The type information of a literal negative or positive integer value."""


class IntLiteralType(IntegralLiteralType):
    """The type information of the default literal negative or positive integer value."""
    def __init__(self):
        super().__init__(constant_types['Int'])


class LongLiteralType(IntegralLiteralType):
    """The type information of a long (8 byte) literal negative or positive integer value."""
    def __init__(self):
        super().__init__(constant_types['Long'])


class FloatingPointLiteralType(NumericLiteralType):
    """The type information of a literal floating-point value."""


class FloatLiteralType(FloatingPointLiteralType):
    """The type information of a literal float (4 byte) value."""
    def __init__(self):
        super().__init__(constant_types['Float'])


class DoubleLiteralType(FloatingPointLiteralType):
    """The type information of a literal double (8 byte) value."""
    def __init__(self):
        super().__init__(constant_types['Double'])


class StringLiteralType(LiteralType):
    """The type information of a string literal."""
    def __init__(self):
        super().__init__(constant_types['String'])


class BoolLiteralType(LiteralType):
    """The type information of a literal boolean value."""
    def __init__(self):
        super().__init__(constant_types['Bool'])

