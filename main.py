from compiler.compile import compile_from_file


def main():

    compile_from_file('examples/test.shf', regenerate_grammar=True)


if __name__ == "__main__":
    main()
