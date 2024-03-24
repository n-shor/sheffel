from ..structure.abstract import Node

from . import Translator


class Assembler(Translator[Node, str]):
    """Translates abstract node representation into llvm ir"""
