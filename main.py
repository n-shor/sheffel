from compiler.ast.nodes import *
from compiler.ast.types import *

from compiler.compile import compile_file


code = """
noread Int& y
noread Int& x = 5
x = x + 5
"""


def main():
    compile_file('./code.shf', alternative_code=code, run_ir_generator=False, make_executable=False)


if __name__ == "__main__":
    main()
