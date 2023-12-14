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


    # Enter a parse tree produced by CalcParser#AddSub.
    def enterAddSub(self, ctx:CalcParser.AddSubContext):
        pass

    # Exit a parse tree produced by CalcParser#AddSub.
    def exitAddSub(self, ctx:CalcParser.AddSubContext):
        pass


    # Enter a parse tree produced by CalcParser#MulDev.
    def enterMulDev(self, ctx:CalcParser.MulDevContext):
        pass

    # Exit a parse tree produced by CalcParser#MulDev.
    def exitMulDev(self, ctx:CalcParser.MulDevContext):
        pass


    # Enter a parse tree produced by CalcParser#Int.
    def enterInt(self, ctx:CalcParser.IntContext):
        pass

    # Exit a parse tree produced by CalcParser#Int.
    def exitInt(self, ctx:CalcParser.IntContext):
        pass



del CalcParser