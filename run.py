from compiler.compile import compile_file, BinaryOperator, IntegralLiteral


def main():
    compile_file('./code.shf', alternative_ast=[
        # BinaryOperator('+', BinaryOperator('+', IntegralLiteral(2), IntegralLiteral(1)), IntegralLiteral(8)),
        BinaryOperator('+', IntegralLiteral(5), IntegralLiteral(7))
    ], make_executable=False)


if __name__ == "__main__":
    main()
