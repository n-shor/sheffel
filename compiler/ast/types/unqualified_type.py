from llvmlite import ir


class UnqualifiedType:
    """The base for unqualified type information."""


class NamedUnqualifiedType(UnqualifiedType):
    """An unqualified type represented by a string of its name."""
    def __init__(self, name: str):
        super().__init__()

        self.name = name


class DirectUnqualifiedType(UnqualifiedType):
    """An unqualified type represented by its llvmlite.ir correspondent."""
    def __init__(self, type_: ir.Type):
        super().__init__()

        self.type_ = type_
