from dataclasses import dataclass

from ..types import FunctionType, VariableType, ReferenceMemoryQualifier

from . import Node, Block, VariableDeclaration


@dataclass
class Function(Node):
    """Represents a function creating statement. The function has a type and body."""

    type_: VariableType
    parameters: tuple[VariableDeclaration, ...]
    body: Block

    @classmethod
    def make(cls, return_type: VariableType, parameters: tuple[VariableDeclaration, ...], body: Block):
        return cls(
            VariableType(
                FunctionType(return_type, tuple(p.type_ for p in parameters)),
                ReferenceMemoryQualifier(),
                ()
            ),
            parameters,
            body
        )
