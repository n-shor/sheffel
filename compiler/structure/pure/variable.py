from . import Value, Type, undetermined


class Variable(Value):
    def __init__(self, name: str):
        super().__init__(undetermined)
        self.name = name

    def syntax(self):
        return f'V<"{self.name}":{self.type_.syntax()}>'


class Declaration(Variable):
    def __init__(self, type_: Type, name: str):
        super().__init__(name)
        self.type_ = type_


class Access(Variable):
    def __init__(self, owner: Value, name: str):
        super().__init__(name)
        self.owner = owner

    def syntax(self):
        return f'{self.owner.syntax()} -> {super().syntax()}'
