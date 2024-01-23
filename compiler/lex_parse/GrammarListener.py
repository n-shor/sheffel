# Generated from Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#prog.
    def enterProg(self, ctx:GrammarParser.ProgContext):
        pass

    # Exit a parse tree produced by GrammarParser#prog.
    def exitProg(self, ctx:GrammarParser.ProgContext):
        pass


    # Enter a parse tree produced by GrammarParser#block.
    def enterBlock(self, ctx:GrammarParser.BlockContext):
        pass

    # Exit a parse tree produced by GrammarParser#block.
    def exitBlock(self, ctx:GrammarParser.BlockContext):
        pass


    # Enter a parse tree produced by GrammarParser#EmptyLine.
    def enterEmptyLine(self, ctx:GrammarParser.EmptyLineContext):
        pass

    # Exit a parse tree produced by GrammarParser#EmptyLine.
    def exitEmptyLine(self, ctx:GrammarParser.EmptyLineContext):
        pass


    # Enter a parse tree produced by GrammarParser#ExpressionLine.
    def enterExpressionLine(self, ctx:GrammarParser.ExpressionLineContext):
        pass

    # Exit a parse tree produced by GrammarParser#ExpressionLine.
    def exitExpressionLine(self, ctx:GrammarParser.ExpressionLineContext):
        pass


    # Enter a parse tree produced by GrammarParser#memoryQualifier.
    def enterMemoryQualifier(self, ctx:GrammarParser.MemoryQualifierContext):
        pass

    # Exit a parse tree produced by GrammarParser#memoryQualifier.
    def exitMemoryQualifier(self, ctx:GrammarParser.MemoryQualifierContext):
        pass


    # Enter a parse tree produced by GrammarParser#type.
    def enterType(self, ctx:GrammarParser.TypeContext):
        pass

    # Exit a parse tree produced by GrammarParser#type.
    def exitType(self, ctx:GrammarParser.TypeContext):
        pass


    # Enter a parse tree produced by GrammarParser#behaviorQualifier.
    def enterBehaviorQualifier(self, ctx:GrammarParser.BehaviorQualifierContext):
        pass

    # Exit a parse tree produced by GrammarParser#behaviorQualifier.
    def exitBehaviorQualifier(self, ctx:GrammarParser.BehaviorQualifierContext):
        pass


    # Enter a parse tree produced by GrammarParser#Assignment.
    def enterAssignment(self, ctx:GrammarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by GrammarParser#Assignment.
    def exitAssignment(self, ctx:GrammarParser.AssignmentContext):
        pass


    # Enter a parse tree produced by GrammarParser#Float.
    def enterFloat(self, ctx:GrammarParser.FloatContext):
        pass

    # Exit a parse tree produced by GrammarParser#Float.
    def exitFloat(self, ctx:GrammarParser.FloatContext):
        pass


    # Enter a parse tree produced by GrammarParser#MulDiv.
    def enterMulDiv(self, ctx:GrammarParser.MulDivContext):
        pass

    # Exit a parse tree produced by GrammarParser#MulDiv.
    def exitMulDiv(self, ctx:GrammarParser.MulDivContext):
        pass


    # Enter a parse tree produced by GrammarParser#AddSub.
    def enterAddSub(self, ctx:GrammarParser.AddSubContext):
        pass

    # Exit a parse tree produced by GrammarParser#AddSub.
    def exitAddSub(self, ctx:GrammarParser.AddSubContext):
        pass


    # Enter a parse tree produced by GrammarParser#Var.
    def enterVar(self, ctx:GrammarParser.VarContext):
        pass

    # Exit a parse tree produced by GrammarParser#Var.
    def exitVar(self, ctx:GrammarParser.VarContext):
        pass


    # Enter a parse tree produced by GrammarParser#Parenthesize.
    def enterParenthesize(self, ctx:GrammarParser.ParenthesizeContext):
        pass

    # Exit a parse tree produced by GrammarParser#Parenthesize.
    def exitParenthesize(self, ctx:GrammarParser.ParenthesizeContext):
        pass


    # Enter a parse tree produced by GrammarParser#Declaration.
    def enterDeclaration(self, ctx:GrammarParser.DeclarationContext):
        pass

    # Exit a parse tree produced by GrammarParser#Declaration.
    def exitDeclaration(self, ctx:GrammarParser.DeclarationContext):
        pass


    # Enter a parse tree produced by GrammarParser#Int.
    def enterInt(self, ctx:GrammarParser.IntContext):
        pass

    # Exit a parse tree produced by GrammarParser#Int.
    def exitInt(self, ctx:GrammarParser.IntContext):
        pass



del GrammarParser