from llvmlite import ir

from .unqualified_type import DirectUnqualifiedType


class LiteralType(DirectUnqualifiedType):
    """The type information of a literal value."""
    def __init__(self, type_: ir.Type):
        super().__init__(type_)


class NumericLiteralType(LiteralType):
    """The type information of a numeric literal value."""
    def __init__(self, type_: ir.Type):
        super().__init__(type_)


class IntegralLiteral(NumericLiteralType):
    """The type information of a literal negative or positive integer value."""
    def __init__(self):
        super().__init__(ir.IntType(32))


class FloatingLiteral(NumericLiteralType):
    """The type information of a literal floating-point value."""
    def __init__(self):
        super().__init__(ir.DoubleType())


class StringLiteral(LiteralType):
    """The type information of a string literal."""
    def __init__(self):
        super().__init__(ir.IntType(8).as_pointer())
