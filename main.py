from compiler.compile import compile_from_file


def main():

    compile_from_file('examples/primes.shf', regenerate_grammar=False, print_ir=True, print_result=True)


if __name__ == "__main__":
    main()
