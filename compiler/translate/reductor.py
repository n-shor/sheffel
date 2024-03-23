from ..structure.pure import *

from . import Translator


class Reductor(Translator[Node, ...]):
    """Translates pure ast into reductive ast"""
