
from . import Translator


class Assembler(Translator[...]):
    """Translates reductive ast into llvm ir"""
