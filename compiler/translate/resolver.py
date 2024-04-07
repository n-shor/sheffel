from __future__ import annotations

from ..structure.resolved import scoped
from ..structure import abstract
from ..structure import resolved

from . import ITranslator


class Resolver(scoped.Scope, ITranslator[abstract.Node, resolved.Node]):
    """Resolves operators for function names and variable sub-attributes. Name mangles variables and functions."""

    def __init__(self, parent: Resolver = None):
        super().__init__(parent)

    def translate(self, source):
        return resolved.Node()

# make full tree!
