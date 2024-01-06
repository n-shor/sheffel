from antlr4 import CommonTokenStream, InputStream
from ..ast.nodes import *
from ..ast.types.literal_type import *
from .GrammarLexer import GrammarLexer
from .GrammarParser import GrammarParser
from .GrammarListener import GrammarListener


class GrammarASTBuilder(GrammarListener):
    def __init__(self):
        self.root_node = None
        self.variables = {}  # Store variables (for declarations and assignments)
        # Should I be the one doing the storing??

    def visit(self, ctx):
        # Visit all child nodes recursively
        for child in ctx.getChildren():
            self.visit(child)

        match ctx:
            case GrammarParser.IntContext():
                node = self.exitInt(ctx)
            case GrammarParser.FloatContext():
                node = self.exitFloat(ctx)
            case GrammarParser.AddSubContext():
                node = self.exitAddSub(ctx)
            case GrammarParser.MulDivContext():
                node = self.exitMulDiv(ctx)
            case GrammarParser.VarContext():
                node = self.exitVar(ctx)
            case GrammarParser.AssignmentContext():
                node = self.exitAssignment(ctx)
            case GrammarParser.DeclarationContext():
                node = self.exitDeclaration(ctx)
            case _:
                raise TypeError("No matching context was found.")

        self.handle_ast_node(node)

    # Figure out what this is supposed to do XD
    def handle_ast_node(self, node):
        """
        Handles the placement of a created AST node within the AST structure.
        """
        self.root_node = node if not self.root_node else self.root_node.children.append(node)

    def exitInt(self, ctx: GrammarParser.IntContext):
        return Literal(int(ctx.getText()), IntegralLiteralType())

    def exitFloat(self, ctx: GrammarParser.FloatContext):
        return Literal(float(ctx.getText()), FloatingLiteralType())

    def exitAddSub(self, ctx: GrammarParser.AddSubContext):
        return BinaryOperator(ctx.op, ctx.expr(0), ctx.expr(1))  # change indexes if got an operator instead of an operand / wrong order

    def exitMulDiv(self, ctx: GrammarParser.MulDivContext):
        return BinaryOperator(ctx.op, ctx.expr(0), ctx.expr(1))  # change indexes if got an operator instead of an operand / wrong order

    # This could cause some issues like the parenthesis not showing up or something IDK yet
    def exitFactor(self, ctx: GrammarParser.ParenthesizeContext):
        return self.visit(ctx.expr())  # Does this add the parenthesis to the AST? Do we care if it doesn't?

    def exitVar(self, ctx: GrammarParser.VarContext):
        return Variable(ctx.getText())

    # Not sure what to do here, this should be a binary operator probably, but what about the read and write variables? Should I use them here somehow?
    def exitAssignment(self, ctx: GrammarParser.AssignmentContext):
        """
        var_name = ctx.VAR().getText()
        expr_node = self.visit(ctx.expression())  # Build AST for the expression
        self.variables[var_name] = expr_node  # Store the AST node for the variable
        Should I be doing this?
        """
        return BinaryOperator(ctx.op, ctx.expr(0), ctx.expr(1))

    def exitDeclaration(self, ctx: GrammarParser.DeclarationContext):
        return VariableDeclaration(ctx.VAR(), ctx.type_())

    def exitEmptyLine(self, ctx: GrammarParser.EmptyLineContext):
        return None  # No AST node for empty lines

    def exitExpressionLine(self, ctx: GrammarParser.ExpressionLineContext):
        return self.visit(ctx.expr())  # Build AST for the expression

    def build_ast(self, input_string):
        lexer = GrammarLexer(InputStream(input_string))
        stream = CommonTokenStream(lexer)
        parser = GrammarParser(stream)
        tree = parser.prog()
        self.visit(tree)
        return self.root_node
