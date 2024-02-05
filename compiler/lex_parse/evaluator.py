from antlr4 import CommonTokenStream, InputStream, ParserRuleContext

from .grammar import GrammarLexer
from .grammar import GrammarParser
from .grammar import GrammarListener

from ..ast.nodes import *
from ..ast.types import *


class GrammarASTBuilder(GrammarListener):

    def exit(self, ctx: ParserRuleContext) -> Node | Any:
        """Invokes the correct exit function for the context type and builds the ast from it."""
        # horrific

        t_name = type(ctx).__name__

        if not t_name.endswith("Context"):
            raise TypeError(f"Unknown type {t_name} does not end with \"Context\".")

        ctx_name = t_name[:-7]  # removes the word context

        exit_method = getattr(self, 'exit' + ctx_name, self._error_exit)
        return exit_method(ctx)

    @staticmethod
    def _error_exit(ctx):
        raise TypeError(f"Unknown node type {type(ctx)} was not matched with a method of evaluator.")

    # Program:

    def exitProg(self, ctx: GrammarParser.ProgContext):
        return self.exitMultiLineBlock(ctx)

    # Statement:

    def exitEmptyStat(self, ctx: GrammarParser.EmptyStatContext):
        raise TypeError(f"Attempted to create an empty ast node.")

    def exitExpressionStat(self, ctx: GrammarParser.ExpressionStatContext):
        return self.exit(ctx.expr())

    def exitBlockStat(self, ctx: GrammarParser.BlockStatContext):
        return self.exit(ctx.block())

    def exitReturnStat(self, ctx: GrammarParser.ReturnStatContext):
        subexpression = ctx.expr()
        return Return(self.exit(subexpression)) if subexpression is not None else ReturnVoid()

    # Block:

    def exitMultiLineBlock(self, ctx: GrammarParser.MultiLineBlockContext):
        return Block(tuple(self.exit(s) for s in ctx.stat() if not isinstance(s, GrammarParser.EmptyStatContext)))

    def exitSingleLineBlock(self, ctx: GrammarParser.SingleLineBlockContext):
        return Block((self.exit(ctx.expr()),))

    # Parsing Expression:

    def exitLeftSpacedExpr(self, ctx: GrammarParser.LeftSpacedExprContext):
        return self.exit(ctx.expr())

    def exitRightSpacedExpr(self, ctx: GrammarParser.RightSpacedExprContext):
        return self.exit(ctx.expr())

    def exitParenthesizedExpr(self, ctx: GrammarParser.ParenthesizedExprContext):
        return self.exit(ctx.expr())

    # Literal Expression:

    def exitIntExpr(self, ctx: GrammarParser.IntExprContext):
        return Literal(int(ctx.value.text), IntLiteralType())

    def exitDoubleExpr(self, ctx: GrammarParser.DoubleExprContext):
        return Literal(float(ctx.value.text), DoubleLiteralType())

    def exitBoolExpr(self, ctx: GrammarParser.BoolExprContext):
        return Literal(True if ctx.value.text == "true" else False, BoolLiteralType())

    def exitFloatExpr(self, ctx: GrammarParser.FloatExprContext):
        return Literal(float(ctx.value.text[:-1]), FloatLiteralType())

    def exitLongExpr(self, ctx: GrammarParser.LongExprContext):
        return Literal(int(ctx.value.text[:-1]), LongLiteralType())

    def exitHexExpr(self, ctx: GrammarParser.HexExprContext):
        if ctx.value.text[-1] == 'l' or ctx.value.text[-1] == 'L':
            return Literal(int(ctx.value.text[:-1], 16), LongLiteralType())
        return Literal(int(ctx.value.text, 16), IntLiteralType())

    def exitBinaryExpr(self, ctx: GrammarParser.BinaryExprContext):
        if ctx.value.text[-1] == 'l' or ctx.value.text[-1] == 'L':
            return Literal(int(ctx.value.text[:-2], 2), LongLiteralType())
        return Literal(int(ctx.value.text[:-1], 2), IntLiteralType())

    # Keyword Expression:

    def exitCopyExpr(self, ctx: GrammarParser.CopyExprContext):
        return Copy(self.exit(ctx.expr()))

    def exitViewExpr(self, ctx: GrammarParser.ViewExprContext):
        return View(self.exit(ctx.expr()))

    # Operator Expression:

    def exitCallOpExpr(self, ctx: GrammarParser.CallOpExprContext):
        return Operator('()', tuple(self.exit(e) for e in ctx.expr()))

    def _exit_binary_operator(self, ctx: GrammarParser.ExprContext):
        return Operator(ctx.op.text, (self.exit(ctx.expr(0)), self.exit(ctx.expr(1))))

    def exitMulDivOpExpr(self, ctx: GrammarParser.MulDivOpExprContext):
        return self._exit_binary_operator(ctx)

    def exitAddSubOpExpr(self, ctx: GrammarParser.AddSubOpExprContext):
        return self._exit_binary_operator(ctx)

    def exitAssignOpExpr(self, ctx: GrammarParser.AssignOpExprContext):
        return self._exit_binary_operator(ctx)

    def exitUnarySignOpExpr(self, ctx: GrammarParser.UnarySignOpExprContext):
        return Operator(ctx.op.text, self.exit(ctx.expr()))

    # VariableType:

    @staticmethod
    def _resolve_type_name(ctx: GrammarParser.TypeNameContext) -> UnqualifiedType:
        return NamedUnqualifiedType(ctx.getText())

    @staticmethod
    def _resolve_memory_qualifier(ctx: GrammarParser.MemoryQualifierContext) -> MemoryQualifier:
        match ctx.getText():
            case '&':
                return ValueMemoryQualifier()

            case '*':
                return ReferenceMemoryQualifier()

            case other:
                raise ValueError(f'Unknown signature: "{other}".')

    @staticmethod
    def _resolve_behavior_qualifier(ctx: GrammarParser.BehaviorQualifierContext) -> BehaviorQualifier:
        match ctx.getText():
            case 'noread':
                return NoReadBehaviorQualifier()

            case 'nowrite':
                return NoWriteBehaviorQualifier()

            case other:
                raise ValueError(f'Unknown signature: "{other}".')

    def exitFullVariableType(self, ctx: GrammarParser.FullVariableTypeContext):
        return VariableType(
            self._resolve_type_name(ctx.typeName()),
            self._resolve_memory_qualifier(ctx.memoryQualifier()),
            tuple(self._resolve_behavior_qualifier(q) for q in ctx.behaviorQualifier())
        )

    def exitAutoVariableType(self, ctx: GrammarParser.AutoVariableTypeContext):
        return VariableType(
            AutoUnqualifiedType(),
            self._resolve_memory_qualifier(ctx.memoryQualifier()),
            tuple(self._resolve_behavior_qualifier(q) for q in ctx.behaviorQualifier())
        )

    # Variable Expression:

    def exitVarExpr(self, ctx: GrammarParser.VarExprContext):
        return Variable(ctx.name.text)

    def exitVariableDeclarationExpr(self, ctx: GrammarParser.VariableDeclarationExprContext):
        return VariableDeclaration(ctx.name.text, self.exit(ctx.variableType()))

    # Value Creation

    def exitFunctionCreationExpr(self, ctx: GrammarParser.FunctionCreationExprContext):

        parameters = tuple(self.exit(e) for e in ctx.expr())

        if not all(isinstance(p, VariableDeclaration) for p in parameters):
            raise TypeError(f'Attempted to use a non-variable-declaration as a parameter.')

        return_type = ctx.variableType()

        return Function.make(
            self.exit(return_type) if return_type is not None else VoidType(),
            parameters,
            self.exit(ctx.block())
        )

    # builder:

    def build_ast(self, input_string):
        lexer = GrammarLexer(InputStream(input_string))
        stream = CommonTokenStream(lexer)
        parser = GrammarParser(stream)
        prog = parser.prog()
        return self.exit(prog)
