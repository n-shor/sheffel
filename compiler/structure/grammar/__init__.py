from .utils import regenerate

try:
    from .generated.GrammarLexer import GrammarLexer
    from .generated.GrammarParser import GrammarParser
    from .generated.GrammarVisitor import GrammarVisitor
except ModuleNotFoundError:
    print("Missing grammar files.")
