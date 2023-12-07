# Generated from Calc.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n")
        buf.write(" \4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\7\2\f\n\2\f\2\16")
        buf.write("\2\17\13\2\3\3\3\3\3\3\7\3\24\n\3\f\3\16\3\27\13\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\5\4\36\n\4\3\4\2\2\5\2\4\6\2\4\3\2\5")
        buf.write("\6\3\2\7\b\2\37\2\b\3\2\2\2\4\20\3\2\2\2\6\35\3\2\2\2")
        buf.write("\b\r\5\4\3\2\t\n\t\2\2\2\n\f\5\4\3\2\13\t\3\2\2\2\f\17")
        buf.write("\3\2\2\2\r\13\3\2\2\2\r\16\3\2\2\2\16\3\3\2\2\2\17\r\3")
        buf.write("\2\2\2\20\25\5\6\4\2\21\22\t\3\2\2\22\24\5\6\4\2\23\21")
        buf.write("\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2\26")
        buf.write("\5\3\2\2\2\27\25\3\2\2\2\30\36\7\4\2\2\31\32\7\t\2\2\32")
        buf.write("\33\5\2\2\2\33\34\7\n\2\2\34\36\3\2\2\2\35\30\3\2\2\2")
        buf.write("\35\31\3\2\2\2\36\7\3\2\2\2\5\r\25\35")
        return buf.getvalue()


class CalcParser ( Parser ):

    grammarFileName = "Calc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'-'", 
                     "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "WS", "INT", "PLUS", "MINUS", "MUL", 
                      "DIV", "LPAREN", "RPAREN" ]

    RULE_expr = 0
    RULE_term = 1
    RULE_factor = 2

    ruleNames =  [ "expr", "term", "factor" ]

    EOF = Token.EOF
    WS=1
    INT=2
    PLUS=3
    MINUS=4
    MUL=5
    DIV=6
    LPAREN=7
    RPAREN=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.TermContext)
            else:
                return self.getTypedRuleContext(CalcParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(CalcParser.PLUS)
            else:
                return self.getToken(CalcParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(CalcParser.MINUS)
            else:
                return self.getToken(CalcParser.MINUS, i)

        def getRuleIndex(self):
            return CalcParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = CalcParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.term()
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CalcParser.PLUS or _la==CalcParser.MINUS:
                self.state = 7
                _la = self._input.LA(1)
                if not(_la==CalcParser.PLUS or _la==CalcParser.MINUS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 8
                self.term()
                self.state = 13
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.FactorContext)
            else:
                return self.getTypedRuleContext(CalcParser.FactorContext,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(CalcParser.MUL)
            else:
                return self.getToken(CalcParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(CalcParser.DIV)
            else:
                return self.getToken(CalcParser.DIV, i)

        def getRuleIndex(self):
            return CalcParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = CalcParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.factor()
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CalcParser.MUL or _la==CalcParser.DIV:
                self.state = 15
                _la = self._input.LA(1)
                if not(_la==CalcParser.MUL or _la==CalcParser.DIV):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 16
                self.factor()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CalcParser.INT, 0)

        def LPAREN(self):
            return self.getToken(CalcParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(CalcParser.RPAREN, 0)

        def getRuleIndex(self):
            return CalcParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = CalcParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_factor)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CalcParser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.match(CalcParser.INT)
                pass
            elif token in [CalcParser.LPAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.match(CalcParser.LPAREN)
                self.state = 24
                self.expr()
                self.state = 25
                self.match(CalcParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





