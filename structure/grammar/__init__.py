try:
    from .generated.GrammarLexer import GrammarLexer
    from .generated.GrammarParser import GrammarParser
    from .generated.GrammarListener import GrammarListener
except ModuleNotFoundError:
    print("Missing grammar files.")
from .utils import regenerate
