from compiler.compile import compile_from_code


def main():

    code = """
    String& x = "aaa"
    Char* y = 'a'
    """

    compile_from_code(code, regenerate_grammar=True, print_ir=True, print_result=True)


if __name__ == "__main__":
    main()
