from ast.generate import generate as generate_ast

from ir.generate import generate as generate_ir
from ir.make import make as make_ir

def compile(input_file_path: str):
    
    with open(input_file_path, 'r') as f:
        code = f.read()
    
    expressions, variables = generate_ast(code)
    generate_ir(expressions, variables)
    make_ir()

def main():
    compile('./code.shf')

if __name__ == "__main__":
    main()