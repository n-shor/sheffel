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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write(":\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\f\n\2\r\2\16")
        buf.write("\2\r\3\3\3\3\3\3\3\3\3\3\5\3\25\n\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\5\3\35\n\3\3\3\3\3\5\3!\n\3\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\5\5-\n\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\7\5\65\n\5\f\5\16\58\13\5\3\5\2\3\b\6\2\4\6\b\2\5\3\2")
        buf.write("\5\6\3\2\7\b\3\2\t\n\2@\2\13\3\2\2\2\4 \3\2\2\2\6\"\3")
        buf.write("\2\2\2\b,\3\2\2\2\n\f\5\4\3\2\13\n\3\2\2\2\f\r\3\2\2\2")
        buf.write("\r\13\3\2\2\2\r\16\3\2\2\2\16\3\3\2\2\2\17!\7\3\2\2\20")
        buf.write("\21\5\b\5\2\21\22\7\3\2\2\22!\3\2\2\2\23\25\5\6\4\2\24")
        buf.write("\23\3\2\2\2\24\25\3\2\2\2\25\26\3\2\2\2\26\27\7\17\2\2")
        buf.write("\27\30\7\4\2\2\30\31\5\b\5\2\31\32\7\3\2\2\32!\3\2\2\2")
        buf.write("\33\35\5\6\4\2\34\33\3\2\2\2\34\35\3\2\2\2\35\36\3\2\2")
        buf.write("\2\36\37\7\17\2\2\37!\7\3\2\2 \17\3\2\2\2 \20\3\2\2\2")
        buf.write(" \24\3\2\2\2 \34\3\2\2\2!\5\3\2\2\2\"#\t\2\2\2#\7\3\2")
        buf.write("\2\2$%\b\5\1\2%-\7\r\2\2&-\7\16\2\2\'-\7\17\2\2()\7\13")
        buf.write("\2\2)*\5\b\5\2*+\7\f\2\2+-\3\2\2\2,$\3\2\2\2,&\3\2\2\2")
        buf.write(",\'\3\2\2\2,(\3\2\2\2-\66\3\2\2\2./\f\b\2\2/\60\t\3\2")
        buf.write("\2\60\65\5\b\5\t\61\62\f\7\2\2\62\63\t\4\2\2\63\65\5\b")
        buf.write("\5\b\64.\3\2\2\2\64\61\3\2\2\2\658\3\2\2\2\66\64\3\2\2")
        buf.write("\2\66\67\3\2\2\2\67\t\3\2\2\28\66\3\2\2\2\t\r\24\34 ,")
        buf.write("\64\66")
        return buf.getvalue()


class CalcParser ( Parser ):

    grammarFileName = "Calc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\n'", "'='", "'Int'", "'Float'", "'*'", 
                     "'/'", "'+'", "'-'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "LPAREN", "RPAREN", "INT", "FLOAT", "VAR", 
                      "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_dataType = 2
    RULE_expr = 3

    ruleNames =  [ "prog", "stat", "dataType", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    LPAREN=9
    RPAREN=10
    INT=11
    FLOAT=12
    VAR=13
    WS=14

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

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.StatContext)
            else:
                return self.getTypedRuleContext(CalcParser.StatContext,i)


        def getRuleIndex(self):
            return CalcParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = CalcParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.stat()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CalcParser.T__0) | (1 << CalcParser.T__2) | (1 << CalcParser.T__3) | (1 << CalcParser.LPAREN) | (1 << CalcParser.INT) | (1 << CalcParser.FLOAT) | (1 << CalcParser.VAR))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExpressionLineContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionLine" ):
                listener.enterExpressionLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionLine" ):
                listener.exitExpressionLine(self)


    class EmptyLineContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyLine" ):
                listener.enterEmptyLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyLine" ):
                listener.exitEmptyLine(self)


    class AssignmentLineContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(CalcParser.VAR, 0)
        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)

        def dataType(self):
            return self.getTypedRuleContext(CalcParser.DataTypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentLine" ):
                listener.enterAssignmentLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentLine" ):
                listener.exitAssignmentLine(self)


    class DeclarationLineContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(CalcParser.VAR, 0)
        def dataType(self):
            return self.getTypedRuleContext(CalcParser.DataTypeContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationLine" ):
                listener.enterDeclarationLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationLine" ):
                listener.exitDeclarationLine(self)



    def stat(self):

        localctx = CalcParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = CalcParser.EmptyLineContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.match(CalcParser.T__0)
                pass

            elif la_ == 2:
                localctx = CalcParser.ExpressionLineContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.expr(0)
                self.state = 15
                self.match(CalcParser.T__0)
                pass

            elif la_ == 3:
                localctx = CalcParser.AssignmentLineContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CalcParser.T__2 or _la==CalcParser.T__3:
                    self.state = 17
                    self.dataType()


                self.state = 20
                self.match(CalcParser.VAR)
                self.state = 21
                self.match(CalcParser.T__1)
                self.state = 22
                self.expr(0)
                self.state = 23
                self.match(CalcParser.T__0)
                pass

            elif la_ == 4:
                localctx = CalcParser.DeclarationLineContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CalcParser.T__2 or _la==CalcParser.T__3:
                    self.state = 25
                    self.dataType()


                self.state = 28
                self.match(CalcParser.VAR)
                self.state = 29
                self.match(CalcParser.T__0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalcParser.RULE_dataType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataType" ):
                listener.enterDataType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataType" ):
                listener.exitDataType(self)




    def dataType(self):

        localctx = CalcParser.DataTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_dataType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            _la = self._input.LA(1)
            if not(_la==CalcParser.T__2 or _la==CalcParser.T__3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
            return CalcParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class FloatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(CalcParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalcParser.ExprContext)
            else:
                return self.getTypedRuleContext(CalcParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class VarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(CalcParser.VAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)


    class FactorContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(CalcParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(CalcParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(CalcParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(CalcParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalcParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CalcParser.INT]:
                localctx = CalcParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 35
                self.match(CalcParser.INT)
                pass
            elif token in [CalcParser.FLOAT]:
                localctx = CalcParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 36
                self.match(CalcParser.FLOAT)
                pass
            elif token in [CalcParser.VAR]:
                localctx = CalcParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 37
                self.match(CalcParser.VAR)
                pass
            elif token in [CalcParser.LPAREN]:
                localctx = CalcParser.FactorContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 38
                self.match(CalcParser.LPAREN)
                self.state = 39
                self.expr(0)
                self.state = 40
                self.match(CalcParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 50
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = CalcParser.MulDivContext(self, CalcParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 44
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 45
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CalcParser.T__4 or _la==CalcParser.T__5):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 46
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = CalcParser.AddSubContext(self, CalcParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 47
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 48
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CalcParser.T__6 or _la==CalcParser.T__7):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 49
                        self.expr(6)
                        pass

             
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         




