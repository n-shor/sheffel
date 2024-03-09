from compiler.structure import grammar, pure
from compiler.translate import evaluator


def main():
    grammar.utils.regenerate()

    print(
        evaluator.Evaluator()
        .translate("""
        Int& a = 3
        Int* b = a
        """)
        .hierarchy()
    )


if __name__ == "__main__":
    main()
