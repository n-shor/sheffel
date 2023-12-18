# Generated from calc.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("\35\4\2\t\2\4\3\t\3\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\5\3\20\n\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\30\n\3\f\3\16")
        buf.write("\3\33\13\3\3\3\2\3\4\4\2\4\2\4\3\2\6\7\4\2\5\5\b\b\2\36")
        buf.write("\2\6\3\2\2\2\4\17\3\2\2\2\6\7\5\4\3\2\7\3\3\2\2\2\b\t")
        buf.write("\b\3\1\2\t\n\7\3\2\2\n\13\5\4\3\2\13\f\7\4\2\2\f\20\3")
        buf.write("\2\2\2\r\20\7\n\2\2\16\20\7\t\2\2\17\b\3\2\2\2\17\r\3")
        buf.write("\2\2\2\17\16\3\2\2\2\20\31\3\2\2\2\21\22\f\7\2\2\22\23")
        buf.write("\t\2\2\2\23\30\5\4\3\b\24\25\f\6\2\2\25\26\t\3\2\2\26")
        buf.write("\30\5\4\3\7\27\21\3\2\2\2\27\24\3\2\2\2\30\33\3\2\2\2")
        buf.write("\31\27\3\2\2\2\31\32\3\2\2\2\32\5\3\2\2\2\33\31\3\2\2")
        buf.write("\2\5\17\27\31")
        return buf.getvalue()


class calcParser ( Parser ):

    grammarFileName = "calc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'+'", "'*'", "'/'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "ADD", "MUL", 
                      "DIV", "SUB", "STR", "INT", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_expr = 1

    ruleNames =  [ "prog", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    ADD=3
    MUL=4
    DIV=5
    SUB=6
    STR=7
    INT=8
    NEWLINE=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(calcParser.ExprContext,0)


        def getRuleIndex(self):
            return calcParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = calcParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return calcParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class StrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STR(self):
            return self.getToken(calcParser.STR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStr" ):
                listener.enterStr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStr" ):
                listener.exitStr(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calcParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calcParser.ExprContext)
            else:
                return self.getTypedRuleContext(calcParser.ExprContext,i)

        def MUL(self):
            return self.getToken(calcParser.MUL, 0)
        def DIV(self):
            return self.getToken(calcParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calcParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calcParser.ExprContext)
            else:
                return self.getTypedRuleContext(calcParser.ExprContext,i)

        def ADD(self):
            return self.getToken(calcParser.ADD, 0)
        def SUB(self):
            return self.getToken(calcParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(calcParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)


    class ParenContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(calcParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParen" ):
                listener.enterParen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParen" ):
                listener.exitParen(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = calcParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [calcParser.T__0]:
                localctx = calcParser.ParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 7
                self.match(calcParser.T__0)
                self.state = 8
                self.expr(0)
                self.state = 9
                self.match(calcParser.T__1)
                pass
            elif token in [calcParser.INT]:
                localctx = calcParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 11
                self.match(calcParser.INT)
                pass
            elif token in [calcParser.STR]:
                localctx = calcParser.StrContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 12
                self.match(calcParser.STR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 23
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 21
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = calcParser.MulDivContext(self, calcParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 15
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 16
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==calcParser.MUL or _la==calcParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 17
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = calcParser.AddSubContext(self, calcParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 18
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 19
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==calcParser.ADD or _la==calcParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 20
                        self.expr(5)
                        pass

             
                self.state = 25
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




