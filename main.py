from compiler.compile import compile_from_code


def main():

    code = """0x3fa3f
     01010101010101001010B
    .3F
      3.5
    3L
    """

    result = compile_from_code(code, regenerate_grammar=True, print_ir=False, ir=False, exe=False)
    print(f'{result = }')


if __name__ == "__main__":
    main()
