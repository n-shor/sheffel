from antlr4 import *
from CalcLexer import CalcLexer
from CalcParser import CalcParser
from CalcListener import CalcListener

from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalcParser import CalcParser
else:
    from CalcParser import CalcParser

class CalcEvaluator(CalcListener):
    def __init__(self):
        self.stack = []

    def exitExpr(self, ctx:CalcParser.ExprContext):
        if ctx.getChildCount() == 3:
            right = self.stack.pop()
            left = self.stack.pop()
            op = ctx.getChild(1).getText()
            if op == '+':
                self.stack.append(left + right)
            elif op == '-':
                self.stack.append(left - right)

    def exitTerm(self, ctx:CalcParser.TermContext):
        if ctx.getChildCount() == 3:
            right = self.stack.pop()
            left = self.stack.pop()
            op = ctx.getChild(1).getText()
            if op == '*':
                self.stack.append(left * right)
            elif op == '/':
                self.stack.append(left / right)

    def exitFactor(self, ctx:CalcParser.FactorContext):
        if ctx.getChildCount() == 1:
            self.stack.append(float(ctx.getText()))

    def getValue(self):
        return self.stack.pop() if self.stack else None
