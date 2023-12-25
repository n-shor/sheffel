# Generated from Calc.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,14,85,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,
        1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,4,10,57,8,10,11,
        10,12,10,58,1,11,4,11,62,8,11,11,11,12,11,63,1,11,1,11,4,11,68,8,
        11,11,11,12,11,69,3,11,72,8,11,1,12,4,12,75,8,12,11,12,12,12,76,
        1,13,4,13,80,8,13,11,13,12,13,81,1,13,1,13,0,0,14,1,1,3,2,5,3,7,
        4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,1,0,3,1,
        0,48,57,2,0,65,90,97,122,3,0,9,9,13,13,32,32,90,0,1,1,0,0,0,0,3,
        1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,
        0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,
        0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,1,29,1,0,0,0,3,31,1,0,0,0,5,33,1,
        0,0,0,7,37,1,0,0,0,9,43,1,0,0,0,11,45,1,0,0,0,13,47,1,0,0,0,15,49,
        1,0,0,0,17,51,1,0,0,0,19,53,1,0,0,0,21,56,1,0,0,0,23,61,1,0,0,0,
        25,74,1,0,0,0,27,79,1,0,0,0,29,30,5,10,0,0,30,2,1,0,0,0,31,32,5,
        61,0,0,32,4,1,0,0,0,33,34,5,73,0,0,34,35,5,110,0,0,35,36,5,116,0,
        0,36,6,1,0,0,0,37,38,5,70,0,0,38,39,5,108,0,0,39,40,5,111,0,0,40,
        41,5,97,0,0,41,42,5,116,0,0,42,8,1,0,0,0,43,44,5,42,0,0,44,10,1,
        0,0,0,45,46,5,47,0,0,46,12,1,0,0,0,47,48,5,43,0,0,48,14,1,0,0,0,
        49,50,5,45,0,0,50,16,1,0,0,0,51,52,5,40,0,0,52,18,1,0,0,0,53,54,
        5,41,0,0,54,20,1,0,0,0,55,57,7,0,0,0,56,55,1,0,0,0,57,58,1,0,0,0,
        58,56,1,0,0,0,58,59,1,0,0,0,59,22,1,0,0,0,60,62,7,0,0,0,61,60,1,
        0,0,0,62,63,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,71,1,0,0,0,65,
        67,5,46,0,0,66,68,7,0,0,0,67,66,1,0,0,0,68,69,1,0,0,0,69,67,1,0,
        0,0,69,70,1,0,0,0,70,72,1,0,0,0,71,65,1,0,0,0,71,72,1,0,0,0,72,24,
        1,0,0,0,73,75,7,1,0,0,74,73,1,0,0,0,75,76,1,0,0,0,76,74,1,0,0,0,
        76,77,1,0,0,0,77,26,1,0,0,0,78,80,7,2,0,0,79,78,1,0,0,0,80,81,1,
        0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,83,1,0,0,0,83,84,6,13,0,0,84,
        28,1,0,0,0,7,0,58,63,69,71,76,81,1,6,0,0
    ]

class CalcLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    LPAREN = 9
    RPAREN = 10
    INT = 11
    FLOAT = 12
    VAR = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\n'", "'='", "'Int'", "'Float'", "'*'", "'/'", "'+'", "'-'", 
            "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "LPAREN", "RPAREN", "INT", "FLOAT", "VAR", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "LPAREN", "RPAREN", "INT", "FLOAT", "VAR", "WS" ]

    grammarFileName = "Calc.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


