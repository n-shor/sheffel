from . import Node


class Variable(Node):
    def __init__(self, name: str):
        self.name = name

    def syntax(self):
        return f'"{self.name}"'


class Declaration(Variable):
    def __init__(self, type_: Node, name: str):
        self.type_ = type_
        super().__init__(name)

    def syntax(self):
        return f'{super().syntax()}:{self.type_.syntax()}'


class Access(Variable):
    def __init__(self, owner: Node, name: str):
        super().__init__(name)
        self.owner = owner

    def syntax(self):
        return f'{self.owner.syntax()}->{super().syntax()}'
