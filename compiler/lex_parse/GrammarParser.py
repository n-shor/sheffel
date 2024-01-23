# Generated from Grammar.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,22,185,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,0,1,0,5,0,23,8,0,10,0,12,0,26,
        9,0,1,0,5,0,29,8,0,10,0,12,0,32,9,0,1,0,1,0,1,1,5,1,37,8,1,10,1,
        12,1,40,9,1,1,1,1,1,5,1,44,8,1,10,1,12,1,47,9,1,1,1,1,1,5,1,51,8,
        1,10,1,12,1,54,9,1,1,1,5,1,57,8,1,10,1,12,1,60,9,1,1,1,1,1,5,1,64,
        8,1,10,1,12,1,67,9,1,1,2,5,2,70,8,2,10,2,12,2,73,9,2,1,2,1,2,5,2,
        77,8,2,10,2,12,2,80,9,2,1,2,1,2,5,2,84,8,2,10,2,12,2,87,9,2,1,2,
        1,2,3,2,91,8,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,3,6,103,8,
        6,1,6,1,6,1,6,4,6,108,8,6,11,6,12,6,109,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,5,6,119,8,6,10,6,12,6,122,9,6,1,6,1,6,5,6,126,8,6,10,6,12,6,
        129,9,6,1,6,1,6,3,6,133,8,6,1,6,1,6,5,6,137,8,6,10,6,12,6,140,9,
        6,1,6,1,6,5,6,144,8,6,10,6,12,6,147,9,6,1,6,1,6,1,6,5,6,152,8,6,
        10,6,12,6,155,9,6,1,6,1,6,5,6,159,8,6,10,6,12,6,162,9,6,1,6,1,6,
        1,6,5,6,167,8,6,10,6,12,6,170,9,6,1,6,1,6,5,6,174,8,6,10,6,12,6,
        177,9,6,1,6,5,6,180,8,6,10,6,12,6,183,9,6,1,6,0,1,12,7,0,2,4,6,8,
        10,12,0,5,1,0,4,5,1,0,6,8,1,0,9,10,2,0,4,4,11,11,1,0,12,13,208,0,
        17,1,0,0,0,2,38,1,0,0,0,4,90,1,0,0,0,6,92,1,0,0,0,8,94,1,0,0,0,10,
        96,1,0,0,0,12,132,1,0,0,0,14,16,5,21,0,0,15,14,1,0,0,0,16,19,1,0,
        0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,24,1,0,0,0,19,17,1,0,0,0,20,23,
        3,2,1,0,21,23,3,4,2,0,22,20,1,0,0,0,22,21,1,0,0,0,23,26,1,0,0,0,
        24,22,1,0,0,0,24,25,1,0,0,0,25,30,1,0,0,0,26,24,1,0,0,0,27,29,5,
        21,0,0,28,27,1,0,0,0,29,32,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,
        33,1,0,0,0,32,30,1,0,0,0,33,34,5,0,0,1,34,1,1,0,0,0,35,37,5,21,0,
        0,36,35,1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,41,
        1,0,0,0,40,38,1,0,0,0,41,45,5,1,0,0,42,44,5,21,0,0,43,42,1,0,0,0,
        44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,52,1,0,0,0,47,45,1,
        0,0,0,48,51,3,2,1,0,49,51,3,4,2,0,50,48,1,0,0,0,50,49,1,0,0,0,51,
        54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,58,1,0,0,0,54,52,1,0,0,
        0,55,57,5,21,0,0,56,55,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,
        1,0,0,0,59,61,1,0,0,0,60,58,1,0,0,0,61,65,5,2,0,0,62,64,5,21,0,0,
        63,62,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,3,1,0,
        0,0,67,65,1,0,0,0,68,70,5,21,0,0,69,68,1,0,0,0,70,73,1,0,0,0,71,
        69,1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,0,73,71,1,0,0,0,74,91,5,3,0,
        0,75,77,5,21,0,0,76,75,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,
        1,0,0,0,79,81,1,0,0,0,80,78,1,0,0,0,81,85,3,12,6,0,82,84,5,21,0,
        0,83,82,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,88,
        1,0,0,0,87,85,1,0,0,0,88,89,5,3,0,0,89,91,1,0,0,0,90,71,1,0,0,0,
        90,78,1,0,0,0,91,5,1,0,0,0,92,93,7,0,0,0,93,7,1,0,0,0,94,95,7,1,
        0,0,95,9,1,0,0,0,96,97,7,2,0,0,97,11,1,0,0,0,98,102,6,6,-1,0,99,
        100,3,10,5,0,100,101,5,21,0,0,101,103,1,0,0,0,102,99,1,0,0,0,102,
        103,1,0,0,0,103,104,1,0,0,0,104,105,3,8,4,0,105,107,3,6,3,0,106,
        108,5,21,0,0,107,106,1,0,0,0,108,109,1,0,0,0,109,107,1,0,0,0,109,
        110,1,0,0,0,110,111,1,0,0,0,111,112,5,20,0,0,112,133,1,0,0,0,113,
        133,5,20,0,0,114,133,5,18,0,0,115,133,5,19,0,0,116,120,5,15,0,0,
        117,119,5,21,0,0,118,117,1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,0,
        120,121,1,0,0,0,121,123,1,0,0,0,122,120,1,0,0,0,123,127,3,12,6,0,
        124,126,5,21,0,0,125,124,1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,
        127,128,1,0,0,0,128,130,1,0,0,0,129,127,1,0,0,0,130,131,5,16,0,0,
        131,133,1,0,0,0,132,98,1,0,0,0,132,113,1,0,0,0,132,114,1,0,0,0,132,
        115,1,0,0,0,132,116,1,0,0,0,133,181,1,0,0,0,134,138,10,8,0,0,135,
        137,5,21,0,0,136,135,1,0,0,0,137,140,1,0,0,0,138,136,1,0,0,0,138,
        139,1,0,0,0,139,141,1,0,0,0,140,138,1,0,0,0,141,145,7,3,0,0,142,
        144,5,21,0,0,143,142,1,0,0,0,144,147,1,0,0,0,145,143,1,0,0,0,145,
        146,1,0,0,0,146,148,1,0,0,0,147,145,1,0,0,0,148,180,3,12,6,9,149,
        153,10,7,0,0,150,152,5,21,0,0,151,150,1,0,0,0,152,155,1,0,0,0,153,
        151,1,0,0,0,153,154,1,0,0,0,154,156,1,0,0,0,155,153,1,0,0,0,156,
        160,7,4,0,0,157,159,5,21,0,0,158,157,1,0,0,0,159,162,1,0,0,0,160,
        158,1,0,0,0,160,161,1,0,0,0,161,163,1,0,0,0,162,160,1,0,0,0,163,
        180,3,12,6,8,164,168,10,6,0,0,165,167,5,21,0,0,166,165,1,0,0,0,167,
        170,1,0,0,0,168,166,1,0,0,0,168,169,1,0,0,0,169,171,1,0,0,0,170,
        168,1,0,0,0,171,175,5,14,0,0,172,174,5,21,0,0,173,172,1,0,0,0,174,
        177,1,0,0,0,175,173,1,0,0,0,175,176,1,0,0,0,176,178,1,0,0,0,177,
        175,1,0,0,0,178,180,3,12,6,7,179,134,1,0,0,0,179,149,1,0,0,0,179,
        164,1,0,0,0,180,183,1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,
        13,1,0,0,0,183,181,1,0,0,0,27,17,22,24,30,38,45,50,52,58,65,71,78,
        85,90,102,109,120,127,132,138,145,153,160,168,175,179,181
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'\\n'", "'*'", "'&'", "'Int'", 
                     "'Float'", "'Func'", "'noread'", "'nowrite'", "'/'", 
                     "'+'", "'-'", "'='", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "LPAREN", "RPAREN", 
                      "CUSTOM_OP", "INT", "FLOAT", "VAR", "SPACE", "FULL_SKIP" ]

    RULE_prog = 0
    RULE_block = 1
    RULE_stat = 2
    RULE_memoryQualifier = 3
    RULE_type = 4
    RULE_behaviorQualifier = 5
    RULE_expr = 6

    ruleNames =  [ "prog", "block", "stat", "memoryQualifier", "type", "behaviorQualifier", 
                   "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    LPAREN=15
    RPAREN=16
    CUSTOM_OP=17
    INT=18
    FLOAT=19
    VAR=20
    SPACE=21
    FULL_SKIP=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(GrammarParser.EOF, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SPACE)
            else:
                return self.getToken(GrammarParser.SPACE, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.BlockContext)
            else:
                return self.getTypedRuleContext(GrammarParser.BlockContext,i)


        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StatContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StatContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = GrammarParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 14
                    self.match(GrammarParser.SPACE) 
                self.state = 19
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 24
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 22
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        self.state = 20
                        self.block()
                        pass

                    elif la_ == 2:
                        self.state = 21
                        self.stat()
                        pass

             
                self.state = 26
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 27
                self.match(GrammarParser.SPACE)
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 33
            self.match(GrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SPACE)
            else:
                return self.getToken(GrammarParser.SPACE, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.BlockContext)
            else:
                return self.getTypedRuleContext(GrammarParser.BlockContext,i)


        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.StatContext)
            else:
                return self.getTypedRuleContext(GrammarParser.StatContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = GrammarParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 35
                self.match(GrammarParser.SPACE)
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
            self.match(GrammarParser.T__0)
            self.state = 45
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 42
                    self.match(GrammarParser.SPACE) 
                self.state = 47
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 50
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        self.state = 48
                        self.block()
                        pass

                    elif la_ == 2:
                        self.state = 49
                        self.stat()
                        pass

             
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 55
                self.match(GrammarParser.SPACE)
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 61
            self.match(GrammarParser.T__1)
            self.state = 65
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 62
                    self.match(GrammarParser.SPACE) 
                self.state = 67
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
            return GrammarParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExpressionLineContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SPACE)
            else:
                return self.getToken(GrammarParser.SPACE, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionLine" ):
                listener.enterExpressionLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionLine" ):
                listener.exitExpressionLine(self)


    class EmptyLineContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SPACE)
            else:
                return self.getToken(GrammarParser.SPACE, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyLine" ):
                listener.enterEmptyLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyLine" ):
                listener.exitEmptyLine(self)



    def stat(self):

        localctx = GrammarParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stat)
        self._la = 0 # Token type
        try:
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = GrammarParser.EmptyLineContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==21:
                    self.state = 68
                    self.match(GrammarParser.SPACE)
                    self.state = 73
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 74
                self.match(GrammarParser.T__2)
                pass

            elif la_ == 2:
                localctx = GrammarParser.ExpressionLineContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==21:
                    self.state = 75
                    self.match(GrammarParser.SPACE)
                    self.state = 80
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 81
                self.expr(0)
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==21:
                    self.state = 82
                    self.match(GrammarParser.SPACE)
                    self.state = 87
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 88
                self.match(GrammarParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemoryQualifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_memoryQualifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemoryQualifier" ):
                listener.enterMemoryQualifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemoryQualifier" ):
                listener.exitMemoryQualifier(self)




    def memoryQualifier(self):

        localctx = GrammarParser.MemoryQualifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_memoryQualifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            _la = self._input.LA(1)
            if not(_la==4 or _la==5):
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


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = GrammarParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0)):
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


    class BehaviorQualifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarParser.RULE_behaviorQualifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBehaviorQualifier" ):
                listener.enterBehaviorQualifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBehaviorQualifier" ):
                listener.exitBehaviorQualifier(self)




    def behaviorQualifier(self):

        localctx = GrammarParser.BehaviorQualifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_behaviorQualifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            _la = self._input.LA(1)
            if not(_la==9 or _la==10):
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
            return GrammarParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AssignmentContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SPACE)
            else:
                return self.getToken(GrammarParser.SPACE, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)


    class FloatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(GrammarParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SPACE)
            else:
                return self.getToken(GrammarParser.SPACE, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExprContext,i)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SPACE)
            else:
                return self.getToken(GrammarParser.SPACE, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class VarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(GrammarParser.VAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)


    class ParenthesizeContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(GrammarParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(GrammarParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(GrammarParser.RPAREN, 0)
        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SPACE)
            else:
                return self.getToken(GrammarParser.SPACE, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesize" ):
                listener.enterParenthesize(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesize" ):
                listener.exitParenthesize(self)


    class DeclarationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(GrammarParser.TypeContext,0)

        def memoryQualifier(self):
            return self.getTypedRuleContext(GrammarParser.MemoryQualifierContext,0)

        def VAR(self):
            return self.getToken(GrammarParser.VAR, 0)
        def behaviorQualifier(self):
            return self.getTypedRuleContext(GrammarParser.BehaviorQualifierContext,0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarParser.SPACE)
            else:
                return self.getToken(GrammarParser.SPACE, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a GrammarParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(GrammarParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7, 8, 9, 10]:
                localctx = GrammarParser.DeclarationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9 or _la==10:
                    self.state = 99
                    self.behaviorQualifier()
                    self.state = 100
                    self.match(GrammarParser.SPACE)


                self.state = 104
                self.type_()
                self.state = 105
                self.memoryQualifier()
                self.state = 107 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 106
                    self.match(GrammarParser.SPACE)
                    self.state = 109 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==21):
                        break

                self.state = 111
                self.match(GrammarParser.VAR)
                pass
            elif token in [20]:
                localctx = GrammarParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 113
                self.match(GrammarParser.VAR)
                pass
            elif token in [18]:
                localctx = GrammarParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 114
                self.match(GrammarParser.INT)
                pass
            elif token in [19]:
                localctx = GrammarParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 115
                self.match(GrammarParser.FLOAT)
                pass
            elif token in [15]:
                localctx = GrammarParser.ParenthesizeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 116
                self.match(GrammarParser.LPAREN)
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==21:
                    self.state = 117
                    self.match(GrammarParser.SPACE)
                    self.state = 122
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 123
                self.expr(0)
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==21:
                    self.state = 124
                    self.match(GrammarParser.SPACE)
                    self.state = 129
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 130
                self.match(GrammarParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 181
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 179
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.MulDivContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 134
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 138
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==21:
                            self.state = 135
                            self.match(GrammarParser.SPACE)
                            self.state = 140
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 141
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==11):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 145
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==21:
                            self.state = 142
                            self.match(GrammarParser.SPACE)
                            self.state = 147
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 148
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.AddSubContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 149
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 153
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==21:
                            self.state = 150
                            self.match(GrammarParser.SPACE)
                            self.state = 155
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 156
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 160
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==21:
                            self.state = 157
                            self.match(GrammarParser.SPACE)
                            self.state = 162
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 163
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.AssignmentContext(self, GrammarParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 164
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 168
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==21:
                            self.state = 165
                            self.match(GrammarParser.SPACE)
                            self.state = 170
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 171
                        localctx.op = self.match(GrammarParser.T__13)
                        self.state = 175
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==21:
                            self.state = 172
                            self.match(GrammarParser.SPACE)
                            self.state = 177
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)

                        self.state = 178
                        self.expr(7)
                        pass

             
                self.state = 183
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        self._predicates[6] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         




