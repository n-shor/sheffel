from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from antlr4.tree.Trees import Trees, escapeWhitespace

#from ..ast.nodes import

from .GrammarLexer import GrammarLexer
from .GrammarParser import GrammarParser
from .evaluator import GrammarEvaluator


"""
def get_node_text(node: GrammarParser.ProgContext, rule_names: list[str]):
    return escapeWhitespace(Trees.getNodeText(node, rule_names), False)

def build_expression(tree: GrammarParser.ProgContext, rule_names: list[str]):
    return ...
"""


def create_ast(code: str):
    """Creates an AST from given code."""
    
    input_stream = InputStream(code)
    
    lexer = GrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = GrammarParser(token_stream)

    tree = parser.prog()  # Parse the entire program
    Grammar_evaluator = GrammarEvaluator()
    walker = ParseTreeWalker()
    walker.walk(Grammar_evaluator, tree)
    
    #return build_expression(tree, parser.ruleNames)
    
    return ...