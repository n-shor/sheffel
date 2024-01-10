from antlr4 import CommonTokenStream, InputStream
from ..ast.nodes import *
from ..ast.types.literal_type import *
from .GrammarLexer import GrammarLexer
from .GrammarParser import GrammarParser
from .GrammarListener import GrammarListener


class GrammarASTBuilder(GrammarListener):

    def add(self, ctx):
        match ctx:
            case GrammarParser.IntContext():
                return self.exitInt(ctx)

            case GrammarParser.FloatContext():
                return self.exitFloat(ctx)

            case GrammarParser.AddSubContext():
                return self.exitAddSub(ctx)

            case GrammarParser.MulDivContext():
                return self.exitMulDiv(ctx)

            case GrammarParser.VarContext():
                return self.exitVar(ctx)

            case GrammarParser.AssignmentContext():
                return self.exitAssignment(ctx)

            case GrammarParser.DeclarationContext():
                return self.exitDeclaration(ctx)

            case GrammarParser.ProgContext():
                return self.exitProg(ctx)

            case GrammarParser.ExpressionLineContext():
                return self.exitExpressionLine(ctx)

            case _:
                raise TypeError(f"No matching context was found. Current context: {repr(ctx)}")

    def exitInt(self, ctx: GrammarParser.IntContext):
        print("int")
        return Literal(int(ctx.getText()), IntegralLiteralType())

    def exitFloat(self, ctx: GrammarParser.FloatContext):
        print("float")
        return Literal(float(ctx.getText()), FloatingLiteralType())

    def exitAddSub(self, ctx: GrammarParser.AddSubContext):
        print("addsub")
        return BinaryOperator(ctx.op, self.add(ctx.getChild(0, GrammarParser.ExprContext)),
                              self.add(ctx.getChild(1, GrammarParser.ExprContext)))

    def exitMulDiv(self, ctx: GrammarParser.MulDivContext):
        print("muldiv")
        return BinaryOperator(ctx.op,
                              self.add(ctx.getChild(0, GrammarParser.ExprContext)),
                              self.add(ctx.getChild(1, GrammarParser.ExprContext)))

    def exitFactor(self, ctx: GrammarParser.ParenthesizeContext):
        print("factor")
        return self.add(ctx.getChild(0, GrammarParser.ExprContext))

    def exitVar(self, ctx: GrammarParser.VarContext):
        print("variable")
        return Variable(ctx.getText())

    # Not sure what to do here, this should be a binary operator probably, but what about the read and write variables? Should I use them here somehow?
    def exitAssignment(self, ctx: GrammarParser.AssignmentContext):
        print("assignment")
        return BinaryOperator(ctx.op, self.add(ctx.getChild(0, GrammarParser.ExprContext)),
                              self.add(ctx.getChild(1, GrammarParser.ExprContext)))

    def exitDeclaration(self, ctx: GrammarParser.DeclarationContext):
        print("declaration")
        return VariableDeclaration(ctx.getChild(0, GrammarParser.VarContext).getText(),
                                   ctx.getChild(0, GrammarParser.Type_Context).getText())

    def exitEmptyLine(self, ctx: GrammarParser.EmptyLineContext):
        print("empty line")
        return None  # No AST node for empty lines

    def exitExpressionLine(self, ctx: GrammarParser.ExpressionLineContext):
        print("expression line")
        return self.add(ctx.getChild(0, GrammarParser.ExprContext))  # Build AST for the expression

    def exitProg(self, ctx: GrammarParser.ProgContext):
        print("prog")
        return Block(*(self.add(c) for c in ctx.getChildren() if not isinstance(c, GrammarParser.EmptyLineContext)))

    def build_ast(self, input_string):
        lexer = GrammarLexer(InputStream(input_string))
        stream = CommonTokenStream(lexer)
        parser = GrammarParser(stream)
        tree = parser.prog()
        print("start2")
        return self.add(tree)
