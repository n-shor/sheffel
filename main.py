from compiler.compile import compile_from_code


def main():

    code = """
    Int* x = 5
    Int& y = copy x

    return 0
    """

    compile_from_code(code, regenerate_grammar=False, print_ir=True, print_result=True, exe=False)


if __name__ == "__main__":
    main()
