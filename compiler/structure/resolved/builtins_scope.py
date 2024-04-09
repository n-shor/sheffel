from . import *


def make_builtins_scope():
    scope = Scope(None)
    scope.register('Int', int_type)
    scope.register('Double', double_type)
    scope.register('Bool', bool_type)
    scope.register('Char', char_type)
    scope.register('String', string_type)

    return scope
