from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from antlr4.tree.Trees import Trees, escapeWhitespace

#from ..ast.nodes import

from .GrammarLexer import GrammarLexer
from .GrammarParser import GrammarParser
from .evaluator import GrammarASTBuilder


"""
def get_node_text(node: GrammarParser.ProgContext, rule_names: list[str]):
    return escapeWhitespace(Trees.getNodeText(node, rule_names), False)

def build_expression(tree: GrammarParser.ProgContext, rule_names: list[str]):
    return ...
"""


def create_ast(code: str):
    """Creates an AST from given code."""
    builder = GrammarASTBuilder()
    return builder.build_ast(code)
