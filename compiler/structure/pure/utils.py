from . import Block, Type, Declaration


def make_declarations_block(**named_types: Type):
    return Block(tuple(
        Declaration(type_, name) for name, type_ in named_types.items()
    ))
