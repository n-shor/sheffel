from compiler.compile import compile_file, BinaryOperator, IntegralLiteral


def main():
    compile_file('./code.shf', alternative_ast=[
        BinaryOperator('+', BinaryOperator('+', IntegralLiteral(2), IntegralLiteral(1)), IntegralLiteral(8))
    ])


if __name__ == "__main__":
    main()
