from antlr4 import *
from CalcLexer import CalcLexer
from CalcParser import CalcParser
from CalcListener import CalcListener

class CalcEvaluator(CalcListener):
    def __init__(self):
        self.stack = []

    def exitExpr(self, ctx:CalcParser.ExprContext):
        # Handle expressions with '+' and '-' operators
        for child in ctx.getChildren():
            if isinstance(child, CalcParser.TermContext):
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

    def exitTerm(self, ctx:CalcParser.TermContext):
        # Handle expressions with '*' and '/' operators
        for child in ctx.getChildren():
            if isinstance(child, CalcParser.FactorContext):
                # Extract and push factor values onto the stack
                value = self.stack.pop()
                self.stack.append(value)
            elif isinstance(child, TerminalNode):
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


    def exitFactor(self, ctx:CalcParser.FactorContext):
        # For factors, just push the number onto the stack
        if ctx.getChildCount() == 1:
            self.stack.append(float(ctx.getText()))

    def getValue(self):
        # Get the final value from the stack
        return self.stack.pop() if self.stack else None
