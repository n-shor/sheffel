from compiler.ast.nodes import *
from compiler.ast.types import *

from compiler.compile import compile_file


def main():
    compile_file('', alternative_code='', alternative_ast=Block(
        Return(Literal(0, IntegralLiteralType()))
    ), run_ir_generator=True, make_executable=False)


if __name__ == "__main__":
    main()
