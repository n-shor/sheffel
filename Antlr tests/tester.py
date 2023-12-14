from antlr4 import *
from CalcLexer import CalcLexer
from CalcParser import CalcParser
from calc_evaluator import CalcEvaluator

def main():
    expression = input("Enter an expression: ")
    input_stream = InputStream(expression)
    lexer = CalcLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CalcParser(token_stream)

    tree = parser.exper()
    
    calc_evaluator = CalcEvaluator()
    walker = ParseTreeWalker()
    walker.walk(calc_evaluator, tree)

    result = calc_evaluator.getValue()
    print("Result:", result)

if __name__ == "__main__":
    main()
