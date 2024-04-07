from __future__ import annotations

from ..structure import scope
from ..structure import abstract
from ..structure import resolved

from . import ITranslator


class Resolver(scope.Scope[resolved.Variable], ITranslator[abstract.Node, resolved.Node]):
    """Resolves variable names and ir typing in an abstract node structure.
    It is responsible for evaluating eval-qualified variables."""

    def __init__(self, parent: Resolver = None):
        super().__init__(parent)

    def translate(self, source):
        return resolved.Node()

# make full tree!
