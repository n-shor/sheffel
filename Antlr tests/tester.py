from antlr4 import *
from CalcLexer import CalcLexer
from CalcParser import CalcParser
from calc_evaluator import CalcEvaluator

def main():
    file_path = "code.shf"  # Fixed file name
    with open(file_path, "r") as file:
        input_stream = InputStream(file.read())

    lexer = CalcLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CalcParser(token_stream)

    tree = parser.prog()  # Parse the entire program

    calc_evaluator = CalcEvaluator()
    walker = ParseTreeWalker()
    walker.walk(calc_evaluator, tree)

    print("AST:")
    print(tree.toStringTree(recog=parser))  # Print the AST

if __name__ == "__main__":
    main()
