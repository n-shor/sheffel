from ir.generate import generate
from ir.make import make

def compile(input_file: str, out_file: str):
    #generate(build_ast(input_file))
    make()

def main():
    compile('./code.shf', './program.exe')

if __name__ == "__main__":
    main()