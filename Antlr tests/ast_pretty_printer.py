###################
#                 #
# project imports #
#                 #
###################
from CalcVisitor import calcVisitor
from CalcParser import calcParser

class ASTPrettyPrinter(calcVisitor):

    def __init__(self) -> None:
        self.index = ""

    @staticmethod
    def nodify(index, value) -> str:
        return f"v{index} [label=\"{value}\"];"

    @staticmethod
    def edgify(i, j) -> str:
        return f"v{i} -> v{j};"

    def visitExpr(self, ctx):
        i = self.index + "0"
        j = self.index + "1"
        p = self.nodify(i, "prog")
        header = "digraph {"
        footer = "}"
        # e = self.visit(ctx.expr())
        #edge = self.edgify(i, j)
        print(p)
        print(ctx)
        return header + p + footer# + e + edge

    def visitInt(self, ctx) -> str:
        return self.nodify(self.index, ctx.INT().getText())

    def visitFloat(self, ctx) -> str:
        return self.nodify(self.index, ctx.FLOAT().getText())

    def visitStr(self, ctx) -> str:
        return self.nodify(self.index, ctx.STR().getText())

    def visitMulDiv(self, ctx) -> str:
        index = self.index
        i = self.index + "0"
        j = self.index + "1"
        v = self.nodify(index, "MUL")
        self.index = i; expr0 = self.visit(ctx.expr(0))
        self.index = j; expr1 = self.visit(ctx.expr(1))
        edge0 = self.edgify(index, i)
        edge1 = self.edgify(index, j)
        # if ctx.op.type == calcParser.ADD:
        return v + expr0 + expr1 + edge0 + edge1

    def visitAddSub(self, ctx):
        index = self.index
        i = self.index + "0"
        j = self.index + "1"
        v = self.nodify(index, "ADD")
        self.index = i; expr0 = self.visit(ctx.expr(0))
        self.index = j; expr1 = self.visit(ctx.expr(1))
        edge0 = self.edgify(index, i)
        edge1 = self.edgify(index, j)
        # if ctx.op.type == calcParser.ADD:
        return v + expr0 + expr1 + edge0 + edge1

    def visitParens(self, ctx):
        self.index += "0"
        v = self.visit(ctx.expr())