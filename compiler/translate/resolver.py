from ..structure.abstract import *
from ..structure.resolved import *

from . import Translator
from .utils import transform_matching_attributes


class Resolver(Translator[Node, Node]):
    """Resolves variable names and ir typing in an abstract node structure."""

    def __init__(self):
        PredefinedScope.apply()

    def translate(self, source):

        match source:
            case Block(nodes=nodes):
                with Scope():
                    return Block(tuple(self.translate(node) for node in nodes))

            case Declaration(type_=type_, name=name):
                Scope.register(name, type_)
                return source

            case Access():
                return source

            case Variable(name=name):
                source.type_ = Scope.access(name)
                return source

            case Node():
                transform_matching_attributes(source, Node, self.translate)
                return source


# variable registration:
# A. add a "resolve" structure package with a "scope" type
# B. some kind of context manager

# variable data:
# the variables themselves are stored in "Variable" instances.
# it has a subclass for builtins.
# (or not, builtins are determined by string name, or by pre-existing in every scope)
