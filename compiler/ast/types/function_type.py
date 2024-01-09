from typing import Callable

from llvmlite import ir

from . import UnqualifiedType, DirectUnqualifiedType, VariableType, ValueMemoryQualifier


class VoidType(VariableType):
    """The information of a stateless type."""
    def __init__(self):
        super().__init__(DirectUnqualifiedType(ir.VoidType()), ValueMemoryQualifier())


class FunctionType(UnqualifiedType):
    """The unqualified type information of a function as it is declared."""
    def __init__(self, *, parameter_types: tuple[VariableType, ...] = (), return_type: VariableType = VoidType()):
        super().__init__()

        self.parameter_types = parameter_types
        self.return_type = return_type

    def get_direct(self, resolver: Callable[[str], ir.Type]) -> ir.Type:
        return ir.FunctionType(
            self.return_type.get_direct(resolver),
            (t.get_direct(resolver) for t in self.parameter_types)
        )
