from compiler.compile import compile_from_code


def main():

    code = """
    Function* double = Int&(Int& x) { return x * 2 }
    
    if double(3) == 6
    {
        return 1
    }
    else
    {
        return 0
    }
    """

    result = compile_from_code(code, regenerate_grammar=False, print_ir=True)
    print(result)


if __name__ == "__main__":
    main()
