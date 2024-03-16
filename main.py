from compiler.structure import grammar, pure, reductive
from compiler.translate import Translator, Evaluator

code = """
return 3
xd = 4
Int* b = 13
xd& a = 8 - 2 * 2
"""


class Compiler(Translator[str, pure.Node]):
    def __init__(self):
        self.translators = (Evaluator(), )

    def translate(self, source):
        step = source
        for translator in self.translators:
            step = translator.translate(step)
        return step


def main():
    grammar.utils.regenerate()

    result = Compiler().translate(code)

    print(result.hierarchy())


if __name__ == "__main__":
    main()
