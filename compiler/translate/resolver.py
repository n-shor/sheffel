from ..structure import abstract
from ..structure import resolved

from . import Translator


class Resolver(Translator[abstract.Node, abstract.Node]):
    """Resolves variable names and ir typing in an abstract node structure."""

    def translate(self, source):

        match source:
            case abstract.Variable():
                return

            case abstract.Node():
                raise TypeError("Unknown node type.")
