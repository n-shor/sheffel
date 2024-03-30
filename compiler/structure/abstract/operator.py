from . import undetermined, Value


class Operator(Value):
    def __init__(self, operation: str, operands: tuple[Value, ...]):
        super().__init__(undetermined)
        self.operation = operation
        self.operands = operands

    def syntax(self):
        match self.operands:
            case []:
                return f'{self.operation}'

            case [single]:
                return f'{self.operation} {single.syntax()}'

            case [first, *rest]:
                return f'{first.syntax()} {self.operation} {', '.join(item.syntax() for item in rest)}'
