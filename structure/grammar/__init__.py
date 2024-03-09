try:
    from .generated.GrammarLexer import *
    from .generated.GrammarParser import *
    from .generated.GrammarListener import *
except ModuleNotFoundError:
    print("Missing grammar files.")
from .utils import regenerate
