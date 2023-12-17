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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("\62\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\6\6\33")
        buf.write("\n\6\r\6\16\6\34\3\7\6\7 \n\7\r\7\16\7!\3\7\3\7\6\7&\n")
        buf.write("\7\r\7\16\7\'\5\7*\n\7\3\b\6\b-\n\b\r\b\16\b.\3\b\3\b")
        buf.write("\2\2\t\3\3\5\4\7\5\t\6\13\7\r\b\17\t\3\2\4\3\2\62;\5\2")
        buf.write("\13\f\17\17\"\"\2\66\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\3")
        buf.write("\21\3\2\2\2\5\23\3\2\2\2\7\25\3\2\2\2\t\27\3\2\2\2\13")
        buf.write("\32\3\2\2\2\r\37\3\2\2\2\17,\3\2\2\2\21\22\7,\2\2\22\4")
        buf.write("\3\2\2\2\23\24\7\61\2\2\24\6\3\2\2\2\25\26\7/\2\2\26\b")
        buf.write("\3\2\2\2\27\30\7-\2\2\30\n\3\2\2\2\31\33\t\2\2\2\32\31")
        buf.write("\3\2\2\2\33\34\3\2\2\2\34\32\3\2\2\2\34\35\3\2\2\2\35")
        buf.write("\f\3\2\2\2\36 \t\2\2\2\37\36\3\2\2\2 !\3\2\2\2!\37\3\2")
        buf.write("\2\2!\"\3\2\2\2\")\3\2\2\2#%\7\60\2\2$&\t\2\2\2%$\3\2")
        buf.write("\2\2&\'\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2(*\3\2\2\2)#\3\2")
        buf.write("\2\2)*\3\2\2\2*\16\3\2\2\2+-\t\3\2\2,+\3\2\2\2-.\3\2\2")
        buf.write("\2.,\3\2\2\2./\3\2\2\2/\60\3\2\2\2\60\61\b\b\2\2\61\20")
        buf.write("\3\2\2\2\b\2\34!\').\3\b\2\2")
        return buf.getvalue()


class CalcLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    INT = 5
    FLOAT = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'/'", "'-'", "'+'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "INT", "FLOAT", "WS" ]

    grammarFileName = "Calc.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


