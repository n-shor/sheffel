from compiler.compile import compile_from_code


def main():

    code = """
if (a=5) { a=3 }
else if 5   =  6
    {a=3
    }
else {}
    """

    result = compile_from_code(code, regenerate_grammar=True, print_ir=False, ir=False, exe=False)
    print(f'{result = }')


if __name__ == "__main__":
    main()
