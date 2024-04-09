from . import *


_types = {
    'Type': type_type,
    'Int': int_type,
    'Double': double_type,
    'Bool': bool_type,
    'Char': char_type,
    'String': string_type
}


def make_builtins_scope():
    scope = Scope(None)

    for name, type_ in _types.items():
        type_var = EvalVariable(type_type, name)
        type_var.store(None, type_)
        scope.register(name, type_var)

    return scope
