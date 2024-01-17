from dataclasses import dataclass
from typing import Callable

from llvmlite import ir

from .unqualified_type import UnqualifiedType
from .variable_type import VariableType


@dataclass
class FunctionType(UnqualifiedType):
    """The unqualified type information of a function as it is declared."""

    return_type: VariableType
    parameter_types: tuple[VariableType, ...]

    def get_direct(self, resolver: Callable[[str], ir.Type]) -> ir.Type:
        return ir.FunctionType(
            self.return_type.get_direct(resolver),
            (t.get_direct(resolver) for t in self.parameter_types)
        )
