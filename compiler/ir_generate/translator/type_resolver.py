from llvmlite import ir

from ...ast.types import UnqualifiedType


_types: dict[str, ir.Type] = {
    'Int': ir.IntType(32),
    'Float': ir.FloatType()
}


def resolver(name: str) -> ir.Type:
    if result := _types.get(name) is None:
        raise ValueError(f'"{name}" is an unknown type.')

    return result


def resolve(type_: UnqualifiedType) -> ir.Type:
    return type_.get_direct(resolver)
