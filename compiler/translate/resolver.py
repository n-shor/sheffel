from ..structure import scope
from ..structure import abstract
from ..structure import resolved

from . import ITranslator


class Resolver(ITranslator[abstract.Node, resolved.Node], scope.Scope[resolved.Variable]):
    """Resolves variable names and ir typing in an abstract node structure.
    It is responsible for evaluating eval-qualified variables."""

    def translate(self, source):
        return resolved.Node()

# make full tree!
