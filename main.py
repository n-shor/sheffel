from compiler.ast.nodes import *
from compiler.ast.types.unqualified_type import NamedUnqualifiedType
from compiler.ast.types.literal_type import IntegralLiteral

from compiler.compile import compile_file


def main():
    compile_file('./code.shf', alternative_code='', alternative_ast=[
        BinaryOperator('=', VariableDeclaration('x', VariableType(NamedUnqualifiedType("Int"), ValueMemoryQualifier())), Literal(2, IntegralLiteral())),
        BinaryOperator('=', WriteVariable('x'), BinaryOperator('+', Literal(5, IntegralLiteral()), ReadVariable('x')))
    ], make_executable=False)


if __name__ == "__main__":
    main()
