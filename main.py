from compiler.ast.nodes import *
from compiler.compile import compile_file


def main():
    compile_file('./code.shf', alternative_code='', alternative_ast=[
        BinaryOperator('=', VariableDeclaration('x', CompleteType([], 'Int', '&')), IntegralLiteral(2)),
        BinaryOperator('=', WriteVariable('x'), BinaryOperator('+', IntegralLiteral(5), ReadVariable('x')))
    ], make_executable=False)


if __name__ == "__main__":
    main()
