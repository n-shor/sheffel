from antlr4 import CommonTokenStream, InputStream
from ..ast.nodes import *
from ..ast.types.literal_type import *
from .GrammarLexer import GrammarLexer
from .GrammarParser import GrammarParser
from .GrammarListener import GrammarListener


class GrammarASTBuilder(GrammarListener):
    def __init__(self):
        self.root_node = None

    def visit(self, ctx):
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
                raise TypeError(f"No matching context was found. Current context: {ctx}")

        self.handle_ast_node(node)
        return node

    # Figure out what this is supposed to do XD
    def handle_ast_node(self, node):
        """
        Handles the placement of a created AST node within the AST structure.
        """
        self.root_node = node if not self.root_node else self.root_node.children.append(node)

    def exitInt(self, ctx: GrammarParser.IntContext):
        print("int")
        return Literal(int(ctx.getText()), IntegralLiteralType())

    def exitFloat(self, ctx: GrammarParser.FloatContext):
        print("float")
        return Literal(float(ctx.getText()), FloatingLiteralType())

    def exitAddSub(self, ctx: GrammarParser.AddSubContext):
        print("addsub")
        return BinaryOperator(ctx.op, self.visit(ctx.getChild(0, GrammarParser.ExprContext)),
                              self.visit(ctx.getChild(1, GrammarParser.ExprContext)))

    def exitMulDiv(self, ctx: GrammarParser.MulDivContext):
        print("muldiv")
        return BinaryOperator(ctx.op, self.visit(ctx.getChild(0, GrammarParser.ExprContext)),
                              self.visit(ctx.getChild(1, GrammarParser.ExprContext)))

    def exitFactor(self, ctx: GrammarParser.ParenthesizeContext):
        print("factor")
        return self.visit(ctx.getChild(0, GrammarParser.ExprContext))

    def exitVar(self, ctx: GrammarParser.VarContext):
        print("variable")
        return Variable(ctx.getText())

    # Not sure what to do here, this should be a binary operator probably, but what about the read and write variables? Should I use them here somehow?
    def exitAssignment(self, ctx: GrammarParser.AssignmentContext):
        print("assignment")
        return BinaryOperator(ctx.op, self.visit(ctx.getChild(0, GrammarParser.ExprContext)),
                              self.visit(ctx.getChild(1, GrammarParser.ExprContext)))

    def exitDeclaration(self, ctx: GrammarParser.DeclarationContext):
        print("declaration")
        return VariableDeclaration(ctx.getChild(0, GrammarParser.VarContext).getText(),
                                   ctx.getChild(0, GrammarParser.Type_Context).getText())

    def exitEmptyLine(self, ctx: GrammarParser.EmptyLineContext):
        print("empty line")
        return None  # No AST node for empty lines

    def exitExpressionLine(self, ctx: GrammarParser.ExpressionLineContext):
        print("expression line")
        return self.visit(ctx.getChild(0, GrammarParser.ExprContext))  # Build AST for the expression

    def build_ast(self, input_string):
        lexer = GrammarLexer(InputStream(input_string))
        stream = CommonTokenStream(lexer)
        parser = GrammarParser(stream)
        tree = parser.prog()
        print("start2")
        self.visit(tree)
        return self.root_node
