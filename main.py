from compiler.ast.nodes import *
from compiler.compile import compile_file


def main():
    compile_file('./code.shf', alternative_code='', alternative_ast=[
        VariableDeclaration('x', CompleteType([], 'Int', '&')),
        BinaryOperator('=', WriteVariable('x'), BinaryOperator('+', IntegralLiteral(2), IntegralLiteral(1))),
        BinaryOperator('=', WriteVariable('x'), BinaryOperator('+', IntegralLiteral(5), ReadVariable('x')))
    ], make_executable=False)


if __name__ == "__main__":
    main()
