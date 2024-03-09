import antlr4 as ant
from ..structure.pure import *
from ..structure.grammar import *

from . import Translator


class Evaluator(Translator[str, Node], GrammarListener):

    def translate(self, source):
        lexer = GrammarLexer(ant.InputStream(source))
        stream = ant.CommonTokenStream(lexer)
        parser = GrammarParser(stream)

        return self.prog(parser.prog())

    def prog(self, context: GrammarParser.ProgContext):
        return Block(tuple(self.stat(s) for s in context.stat()))

    def block(self, context: GrammarParser.BlockContext):

        match context:

            case GrammarParser.MultiLineBlockContext() as ctx:
                return Block(tuple(self.stat(s) for s in ctx.stat()))

            case GrammarParser.SingleLineBlockContext() as ctx:
                return Block((self.expr(ctx.expr()),))

            case GrammarParser.IfBlockContext() as ctx:
                raise NotImplementedError()

            case GrammarParser.WhileBlockContext() as ctx:
                raise NotImplementedError()

            case _ as ctx:
                raise TypeError(f"Unknown type {type(ctx)} is not a block context.")

    def stat(self, context: GrammarParser.StatContext):

        match context:

            case GrammarParser.ExpressionStatContext() as ctx:
                return self.expr(ctx.expr())

            case GrammarParser.BlockStatContext() as ctx:
                return self.block(ctx.block())

            case GrammarParser.ReturnStatContext() as ctx:
                returnee = ctx.expr()
                return Operator('return', (self.expr(returnee),) if returnee is not None else ())

            case _ as ctx:
                raise TypeError(f"Unknown type {type(ctx)} is not a statement context.")

    def expr(self, context: GrammarParser.ExprContext):

        match context:

            case (GrammarParser.LeftSpacedExprContext() |
                  GrammarParser.RightSpacedExprContext() |
                  GrammarParser.ParenthesizedExprContext()) as ctx:
                return self.expr(ctx.expr())

            case GrammarParser.CallOpExprContext() as ctx:
                return Operator('()', tuple(self.expr(e) for e in ctx.expr()))

            case (GrammarParser.UnaryOpExprContext() |
                  GrammarParser.MulDivModOpExprContext() |
                  GrammarParser.AddSubOpExprContext() |
                  GrammarParser.CompareOpExprContext() |
                  GrammarParser.AssignOpExprContext()) as ctx:
                return Operator(ctx.op.text, tuple(self.expr(e) for e in ctx.expr()))

            case GrammarParser.DeclarationExprContext() as ctx:
                return Declaration(self.expr(ctx.expr()), ctx.name.text)

            case GrammarParser.VarExprContext() as ctx:
                return Variable(ctx.name.text)

            case GrammarParser.QualifiedTypeExprContext() as ctx:
                return Qualified(ctx.type_name.text, self.memory(ctx.memory))

            case GrammarParser.ReturningFunctionExprContext() as ctx:
                return_type, *argument_types = (self.expr(e) for e in ctx.expr())
                body = self.block(ctx.block())
                return Function(return_type, argument_types, body)

            case GrammarParser.VoidFunctionExprContext() as ctx:
                raise NotImplementedError()

            case GrammarParser.TypedArrayExprContext() as ctx:
                element_type, *values = (self.expr(e) for e in ctx.expr())
                return Array(element_type, values)

            case GrammarParser.UntypedArrayExprContext() as ctx:
                raise NotImplementedError()

            case GrammarParser.IntExprContext() as ctx:
                return Literal(unsigned_int_type, int(ctx.value.text))

            case _ as ctx:
                raise TypeError(f"Unknown type {type(ctx)} is not a statement context.")

    def memory(self, context: GrammarParser.MemoryContext):

        match context:
            case GrammarParser.EvalMemoryContext():
                return Memory.EVAL

            case GrammarParser.CopyMemoryContext():
                return Memory.COPY

            case GrammarParser.RefMemoryContext():
                return Memory.REF

            case _ as ctx:
                raise TypeError(f"Unknown type {type(ctx)} is not a memory context.")
