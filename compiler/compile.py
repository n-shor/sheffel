from .ast.nodes import *

from .lex_parse.create import create_ast

#from .ir_generate.create import create_ir
#from .ir_generate.make import make

def compile(input_file_path: str):
    with open(input_file_path, 'r') as f:
        code = f.read()
    
    tree = create_ast(code)
    tree = [
        BinaryOperator('+', BinaryOperator('+', IntegralLiteral(2), IntegralLiteral(1)), IntegralLiteral(8))
    ]
    
    #create_ir(tree)
    #make()

