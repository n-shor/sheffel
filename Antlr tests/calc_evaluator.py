from antlr4 import *
from CalcLexer import CalcLexer
from CalcParser import CalcParser
from CalcListener import CalcListener

class CalcEvaluator(CalcListener):
    def __init__(self):
        self.list = []

    def exitInt(self, ctx: CalcParser.IntContext):
        self.list.append(int(ctx.getText()))

    def exitFloat(self, ctx: CalcParser.FloatContext):
        self.list.append(float(ctx.getText()))

    def exitAddSub(self, ctx: CalcParser.AddSubContext):
        # Handle expressions with '+' and '-' operators
        for child in ctx.getChildren():
            if isinstance(child, CalcParser.MulDivContext):
                # Extract and push term values onto the list
                value = self.list.pop()
                self.list.append(value)
            elif isinstance(child, TerminalNode):
                # Handle operators: +, -
                op = child.getText()
                right = self.list.pop()
                left = self.list.pop()
                if op == '+':
                    self.list.append(left + right)
                elif op == '-':
                    self.list.append(left - right)

        # Final value is at the top of the list
        self.list.append(self.list.pop())

    def exitMulDiv(self, ctx: CalcParser.MulDivContext):
        # Handle expressions with '*' and '/' operators
        for child in ctx.getChildren():
            if isinstance(child, CalcParser.FactorContext):
                # Extract and push factor values onto the list
                value = self.list.pop()
                self.list.append(value)
            if isinstance(child, TerminalNode):
                # Handle operators: *, /
                op = child.getText()
                right = self.list.pop()
                left = self.list.pop()
                if op == '*':
                    self.list.append(left * right)
                elif op == '/':
                    self.list.append(left / right)

        # Final value is at the top of the list
        self.list.append(self.list.pop())

    def exitFactor(self, ctx: CalcParser.FactorContext):
        if ctx.getChildCount() == 1:
            self.list.append(float(ctx.getText()))

            
    def getValue(self):
        # Get the final value from the list
        return self.list.pop() if self.list else None
