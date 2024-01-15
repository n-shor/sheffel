from compiler.ast.nodes import *
from compiler.ast.types import *

from compiler.compile import compile_file


def main():

    value_int_t = VariableType(NamedUnqualifiedType('Int'), ValueMemoryQualifier())
    int_int_func_t = FunctionType(parameter_types=(value_int_t, ), return_type=value_int_t)
    function_value = Function(int_int_func_t, Block(Return(Literal(3, IntegralLiteralType()))))

    compile_file('', alternative_code='', alternative_ast=Block(
        BinaryOperator('=',
                       VariableDeclaration('x', function_value.type_),
                       function_value
                       ),
        Return(Literal(0, IntegralLiteralType()))
    ), run_ir_generator=True, make_executable=False)


if __name__ == "__main__":
    main()
