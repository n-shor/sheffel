from llvmlite import ir

from . import Node, Named, VariableDeclaration


class TypeDeclaration(Named):
    def __init__(self, name: str, fields: tuple[VariableDeclaration, ...]):
        """fields are all non-eval attributes."""
        super().__init__(name)
        self.fields = fields
        self.ir_type = ir.LiteralStructType(tuple(field.ir_type for field in fields))

    def syntax(self):
        return f'type {super().syntax()} of {', '.join(field.syntax() for field in self.fields)} as {self.ir_type}'


class TypeInitialization(Node):
    """Initialization by struct constructor; i.e. {}."""
    def __init__(self, type_: TypeDeclaration, values: tuple[Node, ...]):
        self.type_ = type_
        self.values = values
