from compiler.compile import compile_from_code


def main():

    code = """
    if (true)
    {
        
    }
    
    return 0
    """

    result = compile_from_code(code, regenerate_grammar=True, print_ir=False, print_ast=True)
    print(result)


if __name__ == "__main__":
    main()
