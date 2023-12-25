from compiler.compile import *


def main():
    compile_file('./code.shf', alternative_ast=[
        BinaryOperator('=', VariableDeclaration('x', ir.IntType(32)), IntegralLiteral(13)),
        BinaryOperator('=', Variable('x'), BinaryOperator('+', BinaryOperator('-', Variable('x'), IntegralLiteral(3)), IntegralLiteral(8)))
    ], make_executable=False)


if __name__ == "__main__":
    main()
