from antlr4 import *

from .GrammarLexer import GrammarLexer
from .GrammarParser import GrammarParser
from .GrammarListener import GrammarListener

class GrammarEvaluator(GrammarListener):
    def __init__(self):
        self.variables = {}  # Store variables
        self.list = []  # For expression evaluation

    def exitInt(self, ctx: GrammarParser.IntContext):
        self.list.append(int(ctx.getText()))

    def exitFloat(self, ctx: GrammarParser.FloatContext):
        self.list.append(float(ctx.getText()))

    def exitAddSub(self, ctx: GrammarParser.AddSubContext):
        # Handle expressions with '+' and '-' operators
        for child in ctx.getChildren():
            if isinstance(child, GrammarParser.MulDivContext):
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

    def exitMulDiv(self, ctx: GrammarParser.MulDivContext):
        # Handle expressions with '*' and '/' operators
        for child in ctx.getChildren():
            if isinstance(child, GrammarParser.FactorContext):
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

    def exitFactor(self, ctx: GrammarParser.FactorContext):
        if ctx.getChildCount() == 1:
            self.list.append(float(ctx.getText()))

    def exitVar(self, ctx: GrammarParser.VarContext):
        # Handle variable usage
        var_name = ctx.getText()
        value = self.variables.get(var_name)
        self.list.append(value)

    def exitAssignmentLine(self, ctx: GrammarParser.AssignmentLineContext):
        if ctx.dataType():  # Check if a type is specified
            var_type = ctx.dataType().getText()
        else:
            var_type = None  # No type specified
        var_name = ctx.VAR().getText()
        value = self.list.pop()  # Get the expression's value
        self.variables[var_name] = (var_type, value)  # Store type and value

    def exitDeclarationLine(self, ctx: GrammarParser.DeclarationLineContext):
        if ctx.dataType():  # Check if a type is specified
            var_type = ctx.dataType().getText()
        else:
            var_type = None  # No type specified
        var_name = ctx.VAR().getText()
        self.variables[var_name] = (var_type, None)  # Store type, value is None
    
    def exitEmptyLine(self, ctx: GrammarParser.EmptyLineContext):
        return

    def exitExpressionLine(self, ctx: GrammarParser.ExpressionLineContext):
        expr_value = self.list.pop()  # Evaluate the expression

