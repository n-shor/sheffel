from compiler.compile import compile_from_code


def main():

    code = """
    Int& x = 5
    Int& y = 0
    
    while y < 5
    {
        x = x + 1
        y = y + 1
    }

    return x
    """

    compile_from_code(code, regenerate_grammar=False, print_ir=True, print_result=True)


if __name__ == "__main__":
    main()
