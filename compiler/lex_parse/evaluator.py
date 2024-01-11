from antlr4 import CommonTokenStream, InputStream

from .GrammarLexer import GrammarLexer
from .GrammarParser import GrammarParser
from .GrammarListener import GrammarListener

from ..ast.nodes import *
from ..ast.types import *


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
        # if ctx.parentCtx.get:
        # discuss read/write var returning problems with eavri
        return Variable(ctx.getText())

    def exitAssignment(self, ctx: GrammarParser.AssignmentContext):
        print("assignment")
        return BinaryOperator(ctx.op,
                              self.add(ctx.getChild(0, GrammarParser.ExprContext)),
                              self.add(ctx.getChild(1, GrammarParser.ExprContext)))

    @staticmethod
    def resolve_memory_qualifier(signature: str):
        match signature:
            case '&':
                return ValueMemoryQualifier()

            case '*':
                return ReferenceMemoryQualifier()

            case _:
                raise ValueError(f'Unknown signature: "{signature}".')

    @staticmethod
    def resolve_behavior_qualifier(signature: str):
        match signature:
            case 'noread':
                return NoReadBehaviorQualifier()

            case 'nowrite':
                return NoWriteBehaviorQualifier()

            case _:
                raise ValueError(f'Unknown signature: "{signature}".')

    def exitDeclaration(self, ctx: GrammarParser.DeclarationContext):
        print("declaration")

        *_, name = ctx.getChildren()

        if ctx.getChild(0, GrammarParser.BehaviorQualifierContext) is None:
            type_ = VariableType(NamedUnqualifiedType(ctx.getChild(0, GrammarParser.TypeContext).getText()),
                                 self.resolve_memory_qualifier(
                                     ctx.getChild(0, GrammarParser.MemoryQualifierContext).getText()))
        else:
            type_ = VariableType(NamedUnqualifiedType(ctx.getChild(0, GrammarParser.TypeContext).getText()),
                                 self.resolve_memory_qualifier(
                                     ctx.getChild(0, GrammarParser.MemoryQualifierContext).getText()),
                                 self.resolve_behavior_qualifier(
                                     ctx.getChild(0, GrammarParser.BehaviorQualifierContext).getText()))

        return VariableDeclaration(name, type_)

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
