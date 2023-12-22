from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from antlr4.tree.Trees import Trees, escapeWhitespace

from .CalcLexer import CalcLexer
from .CalcParser import CalcParser
from .calc_evaluator import CalcEvaluator

from .expression_tree import Expression

"""
def get_node_text(node: CalcParser.ProgContext, rule_names: list[str]):
    return escapeWhitespace(Trees.getNodeText(node, rule_names), False)

def build_expression(tree: CalcParser.ProgContext, rule_names: list[str]):
    return ...
"""


def generate(code: str):
    
    input_stream = InputStream(code)
    
    lexer = CalcLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CalcParser(token_stream)

    tree = parser.prog()  # Parse the entire program

    calc_evaluator = CalcEvaluator()
    walker = ParseTreeWalker()
    walker.walk(calc_evaluator, tree)
    
    #return build_expression(tree, parser.ruleNames)
    
    return Expression(...)