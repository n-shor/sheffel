from compiler.compile import compile_from_code


def main():

    code = """
    while (true)
    {
        x = 5
    }
    """

    result = compile_from_code(code, regenerate_grammar=True, print_ir=True, print_ast=True)
    print(result)


if __name__ == "__main__":
    main()
