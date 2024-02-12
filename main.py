from compiler.compile import compile_from_code


def main():

    code = """
    Int* x = 5
    Int& y = copy x

    return y
    """

    compile_from_code(code, regenerate_grammar=False, print_result=True, exe=True)


if __name__ == "__main__":
    main()
