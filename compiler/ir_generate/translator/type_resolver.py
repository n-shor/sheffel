from llvmlite import ir

from ...ast.types import UnqualifiedType, VariableType, ValueMemoryQualifier, ReferenceMemoryQualifier


_types: dict[str, ir.Type] = {
    'Int': ir.IntType(32),
    'Float': ir.FloatType()
}


def resolver(name: str) -> ir.Type:
    if (result := _types.get(name)) is None:
        raise ValueError(f'"{name}" is an unknown type.')

    return result


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
