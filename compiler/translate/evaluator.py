import antlr4 as ant

from ..structure.pure import *
from ..structure.grammar import *

from . import Translator


class Evaluator(Translator[str, Node], GrammarVisitor):

    def translate(self, source):
        lexer = GrammarLexer(ant.InputStream(source))
        stream = ant.CommonTokenStream(lexer)
        parser = GrammarParser(stream)
        tree = parser.prog()
        return self.visit(tree)

    def _visit_statements(self, *statements: GrammarParser.StatContext):
        return tuple(self.visit(s) for s in statements if not isinstance(s, GrammarParser.EmptyStatContext))

    # program

    def visitProg(self, ctx: GrammarParser.ProgContext):
        return Block(self._visit_statements(*ctx.stat()))

    # statements

    def visitEmptyStat(self, ctx):
        raise AssertionError("An empty statement should never be visited.")

    def visitExpressionStat(self, ctx):
        return self.visit(ctx.expr())

    def visitBlockStat(self, ctx):
        return self.visit(ctx.block())

    def visitReturnStat(self, ctx):
        return self._visit_operator('return', ctx.expr())

    # blocks

    def visitSingleLineBlock(self, ctx):
        return Block((self.visit(ctx.expr()),))

    def visitMultiLineBlock(self, ctx):
        return Block(self._visit_statements(*ctx.stat()))

    def visitIfBlock(self, ctx):
        raise NotImplementedError()

    def visitWhileBlock(self, ctx):
        raise NotImplementedError()

    # expressions - literals

    def visitIntLiteralExpr(self, ctx):
        return unsigned_int_type.make_literal(int(ctx.getText()))

    def visitDoubleLiteralExpr(self, ctx):
        return double_type.make_literal(float(ctx.getText()))

    # expressions - compositions

    def visitMemoryCompositionExpr(self, ctx):
        return MemoryComposition.from_symbol(ctx.memory.text, self.visit(ctx.expr()))

    def visitFunctionCompositionExpr(self, ctx):
        ret_type, *args = (self.visit(e) for e in ctx.expr())
        body = self.visit(ctx.block())
        return FunctionComposition(ret_type, args, body)

    def visitArrayCompositionExpr(self, ctx):
        elem_type, *vals = (self.visit(e) for e in ctx.expr())
        return ArrayComposition(elem_type, vals)

    # expressions - variables

    def visitVariableExpr(self, ctx):
        return Variable(ctx.name.text)

    def visitDeclarationExpr(self, ctx):
        return Declaration(self.visit(ctx.expr()), ctx.name.text)

    def visitAccessExpr(self, ctx):
        return Access(self.visit(ctx.expr()), ctx.name.text)

    # expressions - operators

    def _visit_operator(self, operation: str, *subexpressions: GrammarParser.ExprContext):
        return Operator(operation, tuple(self.visit(e) for e in subexpressions if e is not None))

    def visitInitializeExpr(self, ctx):
        return self._visit_operator('{}', ctx.expr(), ctx.block())

    def visitCallExpr(self, ctx):
        return self._visit_operator('()', *ctx.expr())

    def visitIndexExpr(self, ctx):
        return self._visit_operator('[]', *ctx.expr())

    def visitMulDivModExpr(self, ctx):
        return self._visit_operator(ctx.op.text, *ctx.expr())

    def visitAddSubExpr(self, ctx):
        return self._visit_operator(ctx.op.text, *ctx.expr())

    def visitCompareExpr(self, ctx):
        return self._visit_operator(ctx.op.text, *ctx.expr())

    def visitAssignExpr(self, ctx):
        return self._visit_operator('=', *ctx.expr())

    # literals - syntax

    def visitParenthesizeExpr(self, ctx):
        return self.visit(ctx.expr())
