from compiler.compile import compile_from_file, compile_from_code


def main():

    code = """
    
    Int* x = 3
    Int* y = view x
    
    x = 8
    y = 0
    
    return x
    """

    compile_from_code(code, regenerate_grammar=False, print_ir=False, print_result=True)


if __name__ == "__main__":
    main()
