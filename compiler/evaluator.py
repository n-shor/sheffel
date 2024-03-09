import antlr4 as ant
from ..structure.pure import *
from ..structure.grammar import *

from . import Translator


class Evaluator(Translator[str, Node], GrammarListener):

    def translate(self, source):
        lexer = GrammarLexer(ant.InputStream(source))
        stream = ant.CommonTokenStream(lexer)
        parser = GrammarParser(stream)

        return self.get(parser.prog())

    def get(self, context: ant.ParserRuleContext):

        match context:

            # Block and Program

            case (GrammarParser.ProgContext() | GrammarParser.MultiLineBlockContext()) as ctx:
                return Block(tuple(self.get(stat) for stat in ctx.stat()))

            case GrammarParser.SingleLineBlockContext() as ctx:
                return Block((self.get(ctx.expr()), ))

            case GrammarParser.IfBlockContext() as ctx:
                return

            case GrammarParser.WhileBlockContext() as ctx:
                return

            # Statement

            case GrammarParser.ExpressionStatContext() as ctx:
                return self.get(ctx.expr())

            case GrammarParser.BlockStatContext() as ctx:
                return self.get(ctx.block())

            case GrammarParser.ReturnStatContext() as ctx:
                returnee = ctx.expr()
                return Operator('return', (self.get(returnee), ) if returnee is not None else ())

            case _ as ctx:
                raise TypeError(f"Unknown type {type(ctx)} was not matched by the evaluator.")
