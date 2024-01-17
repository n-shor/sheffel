from compiler.ast import *

from compiler.compile import compile_file


def main():



    code = """
    Int& y
    {}
    {  }
    {Int* x = 5
    {}
    }
    Float* x = 5
    Float& z=6.0
    x = x+ 5
    x= x /y
    x
    5
    func(1,a , 2 )
    x = 6 * (x + y)
    y = 5 - (7-9)

    7
    6.0
    z
    Func* func = Int*(Int& x) { Int& a = 6 }


    """

    compile_file('', alternative_code=code, run_ir_generator=False, make_executable=False)


if __name__ == "__main__":
    main()
