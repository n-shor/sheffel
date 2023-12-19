from antlr4 import *
from CalcLexer import CalcLexer
from CalcParser import CalcParser
from CalcListener import CalcListener

class CalcEvaluator(CalcListener):
    def __init__(self):
        self.stack = []

    def exitInt(self, ctx: CalcParser.IntContext):
        self.stack.append(int(ctx.getText()))

    def exitFloat(self, ctx: CalcParser.FloatContext):
        self.stack.append(float(ctx.getText()))

    def exitAddSub(self, ctx:CalcParser.AddSubContext):
        # Handle expressions with '+' and '-' operators
        for child in ctx.getChildren():
            if isinstance(child, CalcParser.MulDivContext):
                # Extract and push term values onto the stack
                value = self.stack.pop()
                self.stack.append(value)
            elif isinstance(child, TerminalNode):
                # Handle operators: +, -
                op = child.getText()
                right = self.stack.pop()
                left = self.stack.pop()
                if op == '+':
                    self.stack.append(left + right)
                elif op == '-':
                    self.stack.append(left - right)

        # Final value is at the top of the stack
        self.stack.append(self.stack.pop())

    def exitMulDiv(self, ctx:CalcParser.MulDivContext):
        # Handle expressions with '*' and '/' operators
        for child in ctx.getChildren():
            if isinstance(child, CalcParser.FactorContext):
                # Extract and push factor values onto the stack
                value = self.stack.pop()
                self.stack.append(value)
            if isinstance(child, TerminalNode):
                # Handle operators: *, /
                op = child.getText()
                right = self.stack.pop()
                left = self.stack.pop()
                if op == '*':
                    self.stack.append(left * right)
                elif op == '/':
                    self.stack.append(left / right)

        # Final value is at the top of the stack
        self.stack.append(self.stack.pop())

    def exitFactor(self, ctx: CalcParser.FactorContext):
        if ctx.getChildCount() == 1:
            self.stack.append(float(ctx.getText()))

            
    def getValue(self):
        # Get the final value from the stack
        return self.stack.pop() if self.stack else None
