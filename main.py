from compiler.ast.nodes import *
from compiler.ast.types.unqualified_type import NamedUnqualifiedType
from compiler.ast.types.literal_type import IntegralLiteralType

from compiler.compile import compile_file


code = """
int x = 5
x = x + 5
"""


def main():
    compile_file('./code.shf', alternative_code=code, run_ir_generator=False, make_executable=False)


if __name__ == "__main__":
    main()
