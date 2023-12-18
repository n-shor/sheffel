# Generated from calc.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .calcParser import calcParser
else:
    from calcParser import calcParser

# This class defines a complete listener for a parse tree produced by calcParser.
class calcListener(ParseTreeListener):

    # Enter a parse tree produced by calcParser#prog.
    def enterProg(self, ctx:calcParser.ProgContext):
        pass

    # Exit a parse tree produced by calcParser#prog.
    def exitProg(self, ctx:calcParser.ProgContext):
        pass


    # Enter a parse tree produced by calcParser#Str.
    def enterStr(self, ctx:calcParser.StrContext):
        pass

    # Exit a parse tree produced by calcParser#Str.
    def exitStr(self, ctx:calcParser.StrContext):
        pass


    # Enter a parse tree produced by calcParser#Float.
    def enterFloat(self, ctx:calcParser.FloatContext):
        pass

    # Exit a parse tree produced by calcParser#Float.
    def exitFloat(self, ctx:calcParser.FloatContext):
        pass


    # Enter a parse tree produced by calcParser#MulDiv.
    def enterMulDiv(self, ctx:calcParser.MulDivContext):
        pass

    # Exit a parse tree produced by calcParser#MulDiv.
    def exitMulDiv(self, ctx:calcParser.MulDivContext):
        pass


    # Enter a parse tree produced by calcParser#AddSub.
    def enterAddSub(self, ctx:calcParser.AddSubContext):
        pass

    # Exit a parse tree produced by calcParser#AddSub.
    def exitAddSub(self, ctx:calcParser.AddSubContext):
        pass


    # Enter a parse tree produced by calcParser#Int.
    def enterInt(self, ctx:calcParser.IntContext):
        pass

    # Exit a parse tree produced by calcParser#Int.
    def exitInt(self, ctx:calcParser.IntContext):
        pass


    # Enter a parse tree produced by calcParser#Paren.
    def enterParen(self, ctx:calcParser.ParenContext):
        pass

    # Exit a parse tree produced by calcParser#Paren.
    def exitParen(self, ctx:calcParser.ParenContext):
        pass



del calcParser