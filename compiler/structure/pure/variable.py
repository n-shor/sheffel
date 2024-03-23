from . import Value, Type, undetermined


class Variable(Value):
    def __init__(self, name: str):
        super().__init__(undetermined)
        self.name = name

    def __repr__(self):
        return f'{type(self).__name__}({repr(self.name)})'


class Declaration(Variable):
    def __init__(self, type_: Type, name: str):
        super().__init__(name)
        self.type_ = type_
