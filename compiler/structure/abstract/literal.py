from llvmlite import ir

from . import Node


class Literal(Node):
    def __init__(self, py_value, ir_value: ir.Constant):
        """`py_value` is the python equivalent of the literal.
        `ir_value` is the ir constant represented by the literal."""
        self.py_value = py_value
        self.ir_value = ir_value

    def syntax(self):
        return repr(self.py_value)


class IntLiteral(Literal):
    _type = ir.IntType(32)

    def __init__(self, text: str):
        super().__init__(int(text), self._type(text))


class DoubleLiteral(Literal):
    _type = ir.DoubleType()

    def __init__(self, text: str):
        super().__init__(float(text), self._type(text))


class BoolLiteral(Literal):
    _type = ir.IntType(1)
    _TEXT_TRUE = 'true'
    _TEXT_FALSE = 'false'

    def __init__(self, text: str):
        if text not in (self._TEXT_TRUE, self._TEXT_FALSE):
            raise ValueError(f'Bool literal cannot be created from "{text}".')

        super().__init__(text == self._TEXT_TRUE, self._type(text))


class CharLiteral(Literal):
    _type = ir.IntType(8)

    def __init__(self, text: str):
        super().__init__(text, self._type(f"'{text}'"))


class StrLiteral(Literal):
    _type = ir.IntType(8).as_pointer()

    def __init__(self, text: str):
        super().__init__(text, self._type(f"'{text}'"))
