from compiler.compile import *


def main():
    """compile_file('./code.shf', alternative_ast=[
        VariableDeclaration('x', ir.IntType(32)),
        BinaryOperator('=', Variable('x'), IntegralLiteral(13)),
        BinaryOperator('=', Variable('x'), BinaryOperator('+', BinaryOperator('-', Variable('x'), IntegralLiteral(3)), IntegralLiteral(8)))
    ], make_executable=False)"""
    #compile_file('./code.shf', make_executable=False, run_ir_generator=False)


if __name__ == "__main__":
    main()
