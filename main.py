from compiler.ast import *

from compiler.compile import compile_file


def main():




    code = """Function* func = Int&(Int& x)
    {
        return x + 3
    }
    
    Int& y = func(3)
    """

    compile_file('', alternative_code=code, run_ir_generator=False, make_executable=False, print_generated_ast=True)


if __name__ == "__main__":
    main()
