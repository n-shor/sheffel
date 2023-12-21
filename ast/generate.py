from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from antlr4.tree.Trees import Trees, escapeWhitespace

from .CalcLexer import CalcLexer
from .CalcParser import CalcParser
from .calc_evaluator import CalcEvaluator

def claim_children(tree: CalcParser.ProgContext, rule_names: list[str]):
    
    if tree.getChildCount() == 0:
        yield escapeWhitespace(Trees.getNodeText(tree, rule_names), False)
    
    for i in range(0, tree.getChildCount()):
        yield from claim_children(tree.getChild(i), rule_names)
    


def generate(code: str):
    
    input_stream = InputStream(code)
    
    lexer = CalcLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CalcParser(token_stream)

    tree = parser.prog()  # Parse the entire program

    calc_evaluator = CalcEvaluator()
    walker = ParseTreeWalker()
    walker.walk(calc_evaluator, tree)
    
    yield from claim_children(tree, parser.ruleNames)