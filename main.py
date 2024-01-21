from compiler.compile import compile_from_code


def main():

    code = """Function* func = Int&(Int& x)
    {
        return x + 3
    }
    
    Int& y = func(3)
    """

    compile_from_code(code, regenerate_grammar=True, print_ast=True, ir=False, exe=False)


if __name__ == "__main__":
    main()
