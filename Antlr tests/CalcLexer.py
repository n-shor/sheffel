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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("W\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n")
        buf.write("\3\n\3\13\3\13\3\f\6\f;\n\f\r\f\16\f<\3\r\6\r@\n\r\r\r")
        buf.write("\16\rA\3\r\3\r\6\rF\n\r\r\r\16\rG\5\rJ\n\r\3\16\6\16M")
        buf.write("\n\16\r\16\16\16N\3\17\6\17R\n\17\r\17\16\17S\3\17\3\17")
        buf.write("\2\2\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\33\17\35\20\3\2\5\3\2\62;\4\2C\\c|\5\2\13")
        buf.write("\13\17\17\"\"\2\\\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5!\3\2\2")
        buf.write("\2\7#\3\2\2\2\t\'\3\2\2\2\13-\3\2\2\2\r/\3\2\2\2\17\61")
        buf.write("\3\2\2\2\21\63\3\2\2\2\23\65\3\2\2\2\25\67\3\2\2\2\27")
        buf.write(":\3\2\2\2\31?\3\2\2\2\33L\3\2\2\2\35Q\3\2\2\2\37 \7\f")
        buf.write("\2\2 \4\3\2\2\2!\"\7?\2\2\"\6\3\2\2\2#$\7K\2\2$%\7p\2")
        buf.write("\2%&\7v\2\2&\b\3\2\2\2\'(\7H\2\2()\7n\2\2)*\7q\2\2*+\7")
        buf.write("c\2\2+,\7v\2\2,\n\3\2\2\2-.\7,\2\2.\f\3\2\2\2/\60\7\61")
        buf.write("\2\2\60\16\3\2\2\2\61\62\7-\2\2\62\20\3\2\2\2\63\64\7")
        buf.write("/\2\2\64\22\3\2\2\2\65\66\7*\2\2\66\24\3\2\2\2\678\7+")
        buf.write("\2\28\26\3\2\2\29;\t\2\2\2:9\3\2\2\2;<\3\2\2\2<:\3\2\2")
        buf.write("\2<=\3\2\2\2=\30\3\2\2\2>@\t\2\2\2?>\3\2\2\2@A\3\2\2\2")
        buf.write("A?\3\2\2\2AB\3\2\2\2BI\3\2\2\2CE\7\60\2\2DF\t\2\2\2ED")
        buf.write("\3\2\2\2FG\3\2\2\2GE\3\2\2\2GH\3\2\2\2HJ\3\2\2\2IC\3\2")
        buf.write("\2\2IJ\3\2\2\2J\32\3\2\2\2KM\t\3\2\2LK\3\2\2\2MN\3\2\2")
        buf.write("\2NL\3\2\2\2NO\3\2\2\2O\34\3\2\2\2PR\t\4\2\2QP\3\2\2\2")
        buf.write("RS\3\2\2\2SQ\3\2\2\2ST\3\2\2\2TU\3\2\2\2UV\b\17\2\2V\36")
        buf.write("\3\2\2\2\t\2<AGINS\3\b\2\2")
        return buf.getvalue()


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
            "'\n'", "'='", "'Int'", "'Float'", "'*'", "'/'", "'+'", "'-'", 
            "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "LPAREN", "RPAREN", "INT", "FLOAT", "VAR", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "LPAREN", "RPAREN", "INT", "FLOAT", "VAR", "WS" ]

    grammarFileName = "Calc.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


