# Generated from Calc.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\n")
        buf.write("+\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\3\2\6\2\25\n\2\r\2\16\2\26\3\2\3\2\3")
        buf.write("\3\6\3\34\n\3\r\3\16\3\35\3\4\3\4\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\2\2\n\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\3\2\4\5\2\13\f\17\17\"\"\3\2\62;\2,\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\3\24\3\2\2\2\5\33")
        buf.write("\3\2\2\2\7\37\3\2\2\2\t!\3\2\2\2\13#\3\2\2\2\r%\3\2\2")
        buf.write("\2\17\'\3\2\2\2\21)\3\2\2\2\23\25\t\2\2\2\24\23\3\2\2")
        buf.write("\2\25\26\3\2\2\2\26\24\3\2\2\2\26\27\3\2\2\2\27\30\3\2")
        buf.write("\2\2\30\31\b\2\2\2\31\4\3\2\2\2\32\34\t\3\2\2\33\32\3")
        buf.write("\2\2\2\34\35\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36\6")
        buf.write("\3\2\2\2\37 \7-\2\2 \b\3\2\2\2!\"\7/\2\2\"\n\3\2\2\2#")
        buf.write("$\7,\2\2$\f\3\2\2\2%&\7\61\2\2&\16\3\2\2\2\'(\7*\2\2(")
        buf.write("\20\3\2\2\2)*\7+\2\2*\22\3\2\2\2\5\2\26\35\3\b\2\2")
        return buf.getvalue()


class CalcLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    INT = 2
    PLUS = 3
    MINUS = 4
    MUL = 5
    DIV = 6
    LPAREN = 7
    RPAREN = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "INT", "PLUS", "MINUS", "MUL", "DIV", "LPAREN", "RPAREN" ]

    ruleNames = [ "WS", "INT", "PLUS", "MINUS", "MUL", "DIV", "LPAREN", 
                  "RPAREN" ]

    grammarFileName = "Calc.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


