from compiler.ast.nodes import *
from compiler.ast.types import *

from compiler.compile import compile_file


code = """
Int& y
{}
{  }
{Int* x = 5
}
Float* x = 5
Float& z=6.0
x = x+ 5
x= x /y
x
5
x = 6 * (x + y)
y = 5 - (7-9)

7
6.0
z
 

"""


def main():

    value_int_t = VariableType(NamedUnqualifiedType('Int'), ValueMemoryQualifier())
    function_value = Function(
        value_int_t,
        (VariableDeclaration('x', value_int_t), ),
        Block(
            Return(ReadVariable('x'))
        )
    )

    compile_file('', alternative_code=code, run_ir_generator=False, make_executable=False)


if __name__ == "__main__":
    main()
