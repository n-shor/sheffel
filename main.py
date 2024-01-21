from compiler.compile import compile_from_code


def main():

    code = """Function* func = Int&(Int& x)
    {
        return x + 3
    }
    
    Int& z = 3
    Int& y = func(z)
    
    Function* internal_add = (Double& a, Double& b)
    {
        Double& result = a + b
    }
    
    internal_add(1.0, 2.0)
    
    return 0
    """

    compile_from_code(code, regenerate_grammar=True, print_ir=True, ir=True, exe=False)


if __name__ == "__main__":
    main()
