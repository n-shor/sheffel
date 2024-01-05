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

    def visit(self, ctx):
        # Visit all child nodes recursively
        for child in ctx.getChildren():
            self.visit(child)

        match ctx:
            case GrammarParser.IntContext():
                node = ASTNode("Int", value=int(ctx.getText()))
            case GrammarParser.FloatContext():
                node = ASTNode("Float", value=float(ctx.getText()))
            case GrammarParser.AddSubContext():
                node = ASTNode("AddSub", value=ctx.op)
            case _:
                raise TypeError("No matching context was found")

        self.handle_ast_node(node)
        # ... (add logic for other relevant contexts based on your grammar rules) ...

    def handle_ast_node(self, node):
        """
        Handles the placement of a created AST node within the AST structure.
        """
        self.root_node = node if not self.root_node else self.root_node.children.append(node)

    def exitInt(self, ctx: GrammarParser.IntContext):
        node = Literal(int(ctx.getText()), IntegralLiteralType())
        return node

    def exitFloat(self, ctx: GrammarParser.FloatContext):
        node = ASTNode("Float", value=float(ctx.getText()))
        return node

    def exitAddSub(self, ctx: GrammarParser.AddSubContext):
        node = ASTNode("AddSub")
        for child in ctx.getChildren():
            if isinstance(child, GrammarParser.MulDivContext) or isinstance(child, GrammarParser.ParenthesizeContext):
                node.children.append(self.visit(child))
        return node

    def exitMulDiv(self, ctx: GrammarParser.MulDivContext):
        node = ASTNode("MulDiv")
        for child in ctx.getChildren():
            if isinstance(child, GrammarParser.ParenthesizeContext):
                node.children.append(self.visit(child))
        return node

    def exitFactor(self, ctx: GrammarParser.ParenthesizeContext):
        if ctx.getChildCount() == 1:
            # Handle a single value within parentheses
            node = ASTNode(ctx.getText())
            return node
        else:
            # Recursively build AST for the expression within parentheses
            return self.visit(ctx.getChild(1))

    def exitVar(self, ctx: GrammarParser.VarContext):
        node = ASTNode("Var", value=ctx.getText())
        return node

    def exitAssignment(self, ctx: GrammarParser.AssignmentContext):
        var_name = ctx.VAR().getText()
        expr_node = self.visit(ctx.expression())  # Build AST for the expression
        self.variables[var_name] = expr_node  # Store the AST node for the variable

    def exitDeclaration(self, ctx: GrammarParser.DeclarationContext):
        var_name = ctx.VAR().getText()
        node = ASTNode("Declaration", value=var_name)
        return node

    def exitEmptyLine(self, ctx: GrammarParser.EmptyLineContext):
        return None  # No AST node for empty lines

    def exitExpressionLine(self, ctx: GrammarParser.ExpressionLineContext):
        return self.visit(ctx.expression())  # Build AST for the expression

    def build_ast(self, input_string):
        lexer = GrammarLexer(InputStream(input_string))
        stream = CommonTokenStream(lexer)
        parser = GrammarParser(stream)
        tree = parser.prog()
        self.visit(tree)
        return self.root_node
