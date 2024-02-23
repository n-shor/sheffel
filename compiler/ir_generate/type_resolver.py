from llvmlite import ir

from ..ast.types import UnqualifiedType, VariableType, ValueMemoryQualifier, ReferenceMemoryQualifier
from ..ast.types.literal_type import constant_types


def resolver(name: str) -> ir.Type:
    if (result := constant_types.get(name)) is not None:
        return result

    raise ValueError(f'"{name}" is an unknown type.')


def resolve(type_: UnqualifiedType | VariableType) -> ir.Type:

    unqualified = type_.get_direct(resolver)

    match type_:
        case VariableType(memory=ValueMemoryQualifier()):
            return unqualified

        case VariableType(memory=ReferenceMemoryQualifier()):
            return unqualified.as_pointer()

        case UnqualifiedType():
            return unqualified

        case _:
            raise TypeError(f'{type(type_)} is not a recognised type type.')
