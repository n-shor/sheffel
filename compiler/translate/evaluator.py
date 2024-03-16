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

    # program

    def visitProg(self, ctx: GrammarParser.ProgContext):
        return Block(tuple(self.visit(s) for s in ctx.stat()))

    # statements

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
        return Block(tuple(self.visit(s) for s in ctx.stat()))

    def visitIfBlock(self, ctx):
        raise NotImplementedError()

    def visitWhileBlock(self, ctx):
        raise NotImplementedError()

    # expressions - operators

    def visitCallOpExpr(self, ctx):
        return self._visit_operator('()', *ctx.expr())

    def visitUnaryOpExpr(self, ctx):
        return self._visit_operator(ctx.op.text, ctx.expr())

    def visitMulDivModOpExpr(self, ctx):
        return self._visit_operator(ctx.op.text, *ctx.expr())

    def visitAddSubOpExpr(self, ctx):
        return self._visit_operator(ctx.op.text, *ctx.expr())

    def visitCompareOpExpr(self, ctx):
        return self._visit_operator(ctx.op.text, *ctx.expr())

    def visitAssignOpExpr(self, ctx):
        return self._visit_operator('=', *ctx.expr())

    # expressions - variables

    def visitDeclarationExpr(self, ctx):
        return Declaration(self.visit(ctx.qualified), ctx.name.text)

    def visitVarExpr(self, ctx):
        return Variable(ctx.name.text)

    # expressions - literals

    def visitLiteralExpr(self, ctx):
        return self.visit(ctx.literal())

    # literals

    def visitIntLiteral(self, ctx):
        return Literal(unsigned_int_type, int(ctx.getText()))

    def visitDoubleLiteral(self, ctx):
        raise NotImplementedError()

    def visitQualifiedLiteral(self, ctx):
        return Qualified(
            {'Type': eval_type_type.type_, 'Int': unsigned_int_type}[ctx.type_name.text],
            {'^': Memory.EVAL, '&': Memory.COPY, '*': Memory.REF}[ctx.memory.text]
        )

    def visitFunctionLiteral(self, ctx: GrammarParser.FunctionLiteralContext):
        return FunctionLiteral(
            tuple(self.visit(arg) for arg in ctx.args),
            self.visit(ctx.ret_type),
            self.visit(ctx.block())
        )

    def visitArrayLiteral(self, ctx):
        return ArrayLiteral(tuple(self.visit(val) for val in ctx.vals), self.visit(ctx.elem_type))

    # helpers

    def _visit_operator(self, operator: str, *subexpressions: GrammarParser.ExprContext):
        return Operator(operator, tuple(self.visit(e) for e in subexpressions if e is not None))
