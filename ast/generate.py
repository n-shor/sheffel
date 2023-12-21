from antlr4 import *

import io

from .CalcLexer import CalcLexer
from .CalcParser import CalcParser
from .calc_evaluator import CalcEvaluator

def generate(code: str):
    
    input_stream = InputStream(code)
    
    lexer = CalcLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CalcParser(token_stream)

    tree = parser.prog()  # Parse the entire program

    calc_evaluator = CalcEvaluator()
    walker = ParseTreeWalker()
    walker.walk(calc_evaluator, tree)

    # print(tree.toStringTree(recog=parser))  # Print the AST
    
    return calc_evaluator.list, calc_evaluator.variables