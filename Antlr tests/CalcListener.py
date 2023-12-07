# Generated from Calc.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalcParser import CalcParser
else:
    from CalcParser import CalcParser

# This class defines a complete listener for a parse tree produced by CalcParser.
class CalcListener(ParseTreeListener):

    # Enter a parse tree produced by CalcParser#expr.
    def enterExpr(self, ctx:CalcParser.ExprContext):
        pass

    # Exit a parse tree produced by CalcParser#expr.
    def exitExpr(self, ctx:CalcParser.ExprContext):
        pass


    # Enter a parse tree produced by CalcParser#term.
    def enterTerm(self, ctx:CalcParser.TermContext):
        pass

    # Exit a parse tree produced by CalcParser#term.
    def exitTerm(self, ctx:CalcParser.TermContext):
        pass


    # Enter a parse tree produced by CalcParser#factor.
    def enterFactor(self, ctx:CalcParser.FactorContext):
        pass

    # Exit a parse tree produced by CalcParser#factor.
    def exitFactor(self, ctx:CalcParser.FactorContext):
        pass



del CalcParser