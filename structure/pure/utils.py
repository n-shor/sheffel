from . import Block, Memory, Type, Declaration


def make_declarations_block(**declarations: tuple[Type, Memory]):
    return Block(tuple(
        Declaration(type_, memory, name) for name, (type_, memory) in declarations.items()
    ))
