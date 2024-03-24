from ..structure.abstract import *

from . import Translator


class Resolver(Translator[Node, Node]):
    """Resolves variable names and ir typing in an abstract node structure."""
