from llvmlite import ir

from . import Named, Node, Block, Literal, VariableGet, VariableSet


class FunctionDeclaration(Named):
    def __init__(self, name: str, ir_type: ir.FunctionType, body: Block):
        super().__init__(name)
        self.ir_type = ir_type
        self.body = body

    def syntax(self):
        return f'function {super().syntax()}:{self.ir_type} {self.body.syntax()}'


class FunctionCall(Node):
    def __init__(self, function_name: str, return_to: VariableSet | None, arguments: tuple[VariableGet | Literal, ...]):
        self.function_name = function_name
        self.return_to = return_to
        self.arguments = arguments

    def syntax(self):
        call = f'call {self.function_name} with {', '.join(arg.syntax() for arg in self.arguments)}'

        if self.return_to is None:
            return call

        return f'{self.return_to} to {call}'
