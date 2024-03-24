from . import Block, Value, Type, Declaration, Operator


def make_declarations_block(**named_types: Type):
    return Block(tuple(
        Declaration(type_, name) for name, type_ in named_types.items()
    ))


def initialize(type_: Type, *args: Value):
    return Operator('{}', (type_, *args))
