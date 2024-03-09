from . import Block, Memory, Qualified, Declaration


def make_declarations_block(**declarations: Qualified):
    return Block(tuple(
        Declaration(type_, name) for name, type_ in declarations.items()
    ))
