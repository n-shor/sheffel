import antlr4.tree.Tree
from antlr4 import CommonTokenStream, InputStream

from .GrammarLexer import GrammarLexer
from .GrammarParser import GrammarParser
from .GrammarListener import GrammarListener

from ..ast.nodes import *
from ..ast.types import *


class GrammarASTBuilder(GrammarListener):

    def add(self, ctx):
        class_str = str(type(ctx))
        class_name = class_str.split('.')[-1][:-9]  # Maybe change this later on
        exit_method = getattr(self, 'exit' + class_name, self.default_exit)
        return exit_method(ctx)

    def default_exit(self, ctx):
        print(f"Unknown node type: {type(ctx)}")
        # Handle unknown node types or raise an exception as needed
        return None

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
        # missing the read/write classification

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
        unqualified_type_name = ctx.getChild(0, GrammarParser.TypeContext).getText()
        memory_qualifier_name = ctx.getChild(0, GrammarParser.MemoryQualifierContext).getText()
        behavior_qualifier_names = (child.getText() for child in ctx.getChildren() if isinstance(child, GrammarParser.BehaviorQualifierContext))

        type_ = VariableType(
            NamedUnqualifiedType(unqualified_type_name),
            self.resolve_memory_qualifier(memory_qualifier_name),
            *(self.resolve_behavior_qualifier(name) for name in behavior_qualifier_names)
        )

        return VariableDeclaration(name, type_)

    def exitEmptyLine(self, ctx: GrammarParser.EmptyLineContext):
        print("empty line")
        return None  # No AST node for empty lines

    def exitExpressionLine(self, ctx: GrammarParser.ExpressionLineContext):
        print("expression line")
        return self.add(ctx.getChild(0, GrammarParser.ExprContext))  # Build AST for the expression

    def exitParenthesize(self, ctx: GrammarParser.ParenthesizeContext):
        print("parenthesize")
        return self.add(ctx.getChild(1))

    def exitBlock(self, ctx: GrammarParser.BlockContext):
        print("block")
        return Block(*(self.add(c) for c in ctx.getChildren() if not isinstance(c, GrammarParser.EmptyLineContext)
                       and not isinstance(c, antlr4.tree.Tree.TerminalNodeImpl)))

    def exitProg(self, ctx: GrammarParser.ProgContext):
        print("prog")
        return self.exitBlock(ctx)

    def build_ast(self, input_string):
        lexer = GrammarLexer(InputStream(input_string))
        stream = CommonTokenStream(lexer)
        parser = GrammarParser(stream)
        tree = parser.prog()
        print("start2")
        return self.add(tree)
