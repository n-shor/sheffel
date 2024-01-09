from compiler.ast.nodes import *
from compiler.ast.types import *

from compiler.compile import compile_file


def main():
    compile_file('./code.shf', alternative_code='', alternative_ast=[
        Block(
            BinaryOperator('=',
                           VariableDeclaration('x', VariableType(NamedUnqualifiedType("Int"), ValueMemoryQualifier())),
                           Literal(2, IntegralLiteralType())),

            BinaryOperator('=', WriteVariable('x'),
                           BinaryOperator('+', Literal(5, IntegralLiteralType()), ReadVariable('x'))),

            Return(Literal(0, IntegralLiteralType()))
        )

    ], make_executable=False)


if __name__ == "__main__":
    main()
