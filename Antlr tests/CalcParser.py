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
        buf.write("\"\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\7\2\f\n\2\f\2\16")
        buf.write("\2\17\13\2\3\3\3\3\3\3\7\3\24\n\3\f\3\16\3\27\13\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\5\4 \n\4\3\4\2\2\5\2\4\6\2\4")
        buf.write("\3\2\3\4\3\2\5\6\2\"\2\b\3\2\2\2\4\20\3\2\2\2\6\37\3\2")
        buf.write("\2\2\b\r\5\4\3\2\t\n\t\2\2\2\n\f\5\4\3\2\13\t\3\2\2\2")
        buf.write("\f\17\3\2\2\2\r\13\3\2\2\2\r\16\3\2\2\2\16\3\3\2\2\2\17")
        buf.write("\r\3\2\2\2\20\25\5\6\4\2\21\22\t\3\2\2\22\24\5\6\4\2\23")
        buf.write("\21\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25\26\3\2\2\2")
        buf.write("\26\5\3\2\2\2\27\25\3\2\2\2\30 \7\t\2\2\31\32\7\7\2\2")
        buf.write("\32\33\5\2\2\2\33\34\7\b\2\2\34 \3\2\2\2\35\36\t\2\2\2")
        buf.write("\36 \5\6\4\2\37\30\3\2\2\2\37\31\3\2\2\2\37\35\3\2\2\2")
        buf.write(" \7\3\2\2\2\5\r\25\37")
        return buf.getvalue()


class CalcParser ( Parser ):

    grammarFileName = "Calc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUMBER", "WS" ]

    RULE_expr = 0
    RULE_term = 1
    RULE_factor = 2

    ruleNames =  [ "expr", "term", "factor" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NUMBER=7
    WS=8

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
            while _la==CalcParser.T__0 or _la==CalcParser.T__1:
                self.state = 7
                _la = self._input.LA(1)
                if not(_la==CalcParser.T__0 or _la==CalcParser.T__1):
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
            while _la==CalcParser.T__2 or _la==CalcParser.T__3:
                self.state = 15
                _la = self._input.LA(1)
                if not(_la==CalcParser.T__2 or _la==CalcParser.T__3):
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

        def NUMBER(self):
            return self.getToken(CalcParser.NUMBER, 0)

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def factor(self):
            return self.getTypedRuleContext(CalcParser.FactorContext,0)


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
        self._la = 0 # Token type
        try:
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CalcParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.match(CalcParser.NUMBER)
                pass
            elif token in [CalcParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.match(CalcParser.T__4)
                self.state = 24
                self.expr()
                self.state = 25
                self.match(CalcParser.T__5)
                pass
            elif token in [CalcParser.T__0, CalcParser.T__1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                _la = self._input.LA(1)
                if not(_la==CalcParser.T__0 or _la==CalcParser.T__1):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 28
                self.factor()
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





