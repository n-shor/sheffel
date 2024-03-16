from compiler.structure import grammar, pure
from compiler.translate import evaluator

code = """
return 3
xd = 4
Int* b = 13
xd& a = 8 - 2 * 2
"""


def main():
    grammar.utils.regenerate()

    print(
        evaluator.Evaluator()
        .translate(code)
        .hierarchy()
    )


if __name__ == "__main__":
    main()
