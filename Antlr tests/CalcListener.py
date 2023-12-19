# Generated from Calc.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalcParser import CalcParser
else:
    from CalcParser import CalcParser

# This class defines a complete listener for a parse tree produced by CalcParser.
class CalcListener(ParseTreeListener):

    # Enter a parse tree produced by CalcParser#prog.
    def enterProg(self, ctx:CalcParser.ProgContext):
        pass

    # Exit a parse tree produced by CalcParser#prog.
    def exitProg(self, ctx:CalcParser.ProgContext):
        pass


    # Enter a parse tree produced by CalcParser#Float.
    def enterFloat(self, ctx:CalcParser.FloatContext):
        pass

    # Exit a parse tree produced by CalcParser#Float.
    def exitFloat(self, ctx:CalcParser.FloatContext):
        pass


    # Enter a parse tree produced by CalcParser#MulDiv.
    def enterMulDiv(self, ctx:CalcParser.MulDivContext):
        pass

    # Exit a parse tree produced by CalcParser#MulDiv.
    def exitMulDiv(self, ctx:CalcParser.MulDivContext):
        pass


    # Enter a parse tree produced by CalcParser#AddSub.
    def enterAddSub(self, ctx:CalcParser.AddSubContext):
        pass

    # Exit a parse tree produced by CalcParser#AddSub.
    def exitAddSub(self, ctx:CalcParser.AddSubContext):
        pass


    # Enter a parse tree produced by CalcParser#Factor.
    def enterFactor(self, ctx:CalcParser.FactorContext):
        pass

    # Exit a parse tree produced by CalcParser#Factor.
    def exitFactor(self, ctx:CalcParser.FactorContext):
        pass


    # Enter a parse tree produced by CalcParser#Int.
    def enterInt(self, ctx:CalcParser.IntContext):
        pass

    # Exit a parse tree produced by CalcParser#Int.
    def exitInt(self, ctx:CalcParser.IntContext):
        pass



del CalcParser