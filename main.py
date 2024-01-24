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
        return
    }
    
    internal_add(1.0, 2.0)
    
    return y
    """

    result = compile_from_code(code, regenerate_grammar=True, print_ir=False, ir=True, exe=True)
    print(f'{result = }')


if __name__ == "__main__":
    main()
