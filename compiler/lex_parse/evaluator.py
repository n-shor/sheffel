import antlr4.tree.Tree
from antlr4 import CommonTokenStream, InputStream

from .GrammarLexer import GrammarLexer
from .GrammarParser import GrammarParser
from .GrammarListener import GrammarListener

from ..ast.nodes import *
from ..ast.types import *


class GrammarASTBuilder(GrammarListener):

    def add(self, ctx):
        qualified_class_name = str(type(ctx))
        unqualified_class_name = qualified_class_name.split('.')[-1]
        ctx_type = unqualified_class_name[:-9]  # removes the word 'Context'

        exit_method = getattr(self, 'exit' + ctx_type, self.default_exit)
        return exit_method(ctx)

    def default_exit(self, ctx):
        raise TypeError(f"Unknown node type: {type(ctx)}")

    def exitInt(self, ctx: GrammarParser.IntContext):
        return Literal(int(ctx.getText()), IntLiteralType())

    def exitDouble(self, ctx: GrammarParser.DoubleContext):
        return Literal(float(ctx.getText()), DoubleLiteralType())

    def exitAddSub(self, ctx: GrammarParser.AddSubContext):
        return Operator(ctx.op.text,
                        (self.add(ctx.getChild(0, GrammarParser.ExprContext)),
                         self.add(ctx.getChild(1, GrammarParser.ExprContext))))

    def exitMulDiv(self, ctx: GrammarParser.MulDivContext):
        return Operator(ctx.op.text,
                        (self.add(ctx.getChild(0, GrammarParser.ExprContext)),
                         self.add(ctx.getChild(1, GrammarParser.ExprContext))))

    def exitFactor(self, ctx: GrammarParser.ParenthesizeContext):
        return self.add(ctx.getChild(0, GrammarParser.ExprContext))

    def exitVar(self, ctx: GrammarParser.VarContext):
        return Variable(ctx.getText())

    def exitAssignment(self, ctx: GrammarParser.AssignmentContext):
        return Operator(ctx.op.text,
                        (self.add(ctx.getChild(0, GrammarParser.ExprContext)),
                         self.add(ctx.getChild(1, GrammarParser.ExprContext))))

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

        *_, name = ctx.getChildren()
        name = name.getText()

        unqualified_type_name = ctx.getChild(0, GrammarParser.TypeContext).getText()
        memory_qualifier_name = ctx.getChild(0, GrammarParser.MemoryQualifierContext).getText()
        behavior_qualifier_names = (child.getText() for child in ctx.getChildren() if
                                    isinstance(child, GrammarParser.BehaviorQualifierContext))

        type_ = VariableType(
            NamedUnqualifiedType(unqualified_type_name),
            self.resolve_memory_qualifier(memory_qualifier_name),
            tuple(self.resolve_behavior_qualifier(name) for name in behavior_qualifier_names)
        )

        return VariableDeclaration(name, type_)

    def exitEmptyLine(self, ctx: GrammarParser.EmptyLineContext):
        return None  # No AST node for empty lines

    def exitExpressionLine(self, ctx: GrammarParser.ExpressionLineContext):
        return self.add(ctx.getChild(0, GrammarParser.ExprContext))  # Build AST for the expression

    def exitParenthesize(self, ctx: GrammarParser.ParenthesizeContext):
        return self.add(ctx.getChild(1))

    def exitFuncLiteral(self, ctx: GrammarParser.FuncLiteralContext):
        parameters = []

        # combine the 3 loops into one, it's not hard
        if isinstance(ctx.getChild(0), GrammarParser.TypeContext):  # No behavior
            for i, child in enumerate(ctx.getChildren(GrammarParser.ExprContext)):
                if not isinstance(child, antlr4.tree.Tree.TerminalNodeImpl) and not isinstance(child,
                                                                                               GrammarParser.BlockContext) and i > 2:
                    if not isinstance(child, GrammarParser.DeclarationContext):
                        raise TypeError("Parsing error: Unfitting expression when trying to parse a function parameter")
                    parameters.append(self.add(child))

            return Function.make(
                VariableType(NamedUnqualifiedType(ctx.getChild(0, GrammarParser.TypeContext).getText()),
                             self.resolve_memory_qualifier(ctx.getChild(0, GrammarParser.MemoryQualifierContext).getText()), ()),
                parameters, self.add(ctx.getChild(0, GrammarParser.BlockContext)))

        elif isinstance(ctx.getChild(1), GrammarParser.TypeContext):  # Yes behavior
            for i, child in enumerate(ctx.getChildren(GrammarParser.ExprContext)):
                if not isinstance(child, antlr4.tree.Tree.TerminalNodeImpl) and not isinstance(child,
                                                                                               GrammarParser.BlockContext) and i > 3:
                    if not isinstance(child, GrammarParser.DeclarationContext):
                        raise TypeError("Parsing error: Unfitting expression when trying to parse a function parameter")
                    parameters.append(self.add(child))

            return Function.make(
                VariableType(NamedUnqualifiedType(ctx.getChild(0, GrammarParser.TypeContext).getText()),
                             self.resolve_memory_qualifier(ctx.getChild(0, GrammarParser.MemoryQualifierContext).getText()), ()),  # add behavior qualifier here
                parameters, self.add(ctx.getChild(0, GrammarParser.BlockContext)))

        for i, child in enumerate(ctx.getChildren(GrammarParser.ExprContext)):
            if not isinstance(child, antlr4.tree.Tree.TerminalNodeImpl) and not isinstance(child,
                                                                                           GrammarParser.BlockContext):
                if not isinstance(child, GrammarParser.DeclarationContext):
                    raise TypeError("Parsing error: Unfitting expression when trying to parse a function parameter")
                parameters.append(self.add(child))

        return Function.make(VoidType(), parameters, self.add(ctx.getChild(0, GrammarParser.BlockContext)))

    def exitFuncCall(self, ctx: GrammarParser.FuncCallContext):
        return Operator('()',
                        tuple(self.add(c) for c in ctx.getChildren() if
                              not isinstance(c, GrammarParser.EmptyLineContext) and not isinstance(c,
                                                                                                   antlr4.tree.Tree.TerminalNodeImpl)))

    def exitBlock(self, ctx: GrammarParser.BlockContext):
        return Block(tuple(self.add(c) for c in ctx.getChildren() if
                           not isinstance(c, GrammarParser.EmptyLineContext) and not isinstance(c,
                                                                                                antlr4.tree.Tree.TerminalNodeImpl)))

    def exitProg(self, ctx: GrammarParser.ProgContext):
        return self.exitBlock(ctx)

    def build_ast(self, input_string):
        lexer = GrammarLexer(InputStream(input_string))
        stream = CommonTokenStream(lexer)
        parser = GrammarParser(stream)
        tree = parser.prog()
        return self.add(tree)
