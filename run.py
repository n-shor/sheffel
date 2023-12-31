from llvmlite import ir

from compiler.ast.nodes import *
from compiler.compile import compile_file


def main():
    compile_file('./code.shf', alternative_code='', alternative_ast=[
        VariableDeclaration('x', ir.IntType(32)),
        BinaryOperator('=', Variable('x'), BinaryOperator('+', IntegralLiteral(2), IntegralLiteral(1))),
        BinaryOperator('=', Variable('x'), BinaryOperator('+', IntegralLiteral(5), Variable('x')))
    ], make_executable=False)


if __name__ == "__main__":
    main()
