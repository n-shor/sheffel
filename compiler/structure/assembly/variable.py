from . import Type


class Variable:
    def __init__(self, type_: Type):
        self.ir_type = type_
