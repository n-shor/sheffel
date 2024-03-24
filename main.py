from compiler.structure import grammar, abstract
from compiler.translate import Translator, Evaluator

# Solution:
# COPY = &, REFERENCE = *, EVALUATED = ^
# and are immediately "translated" into:
#   &t -> Copy{t}
#   *t -> Ref{t}
#   ^t -> Eval{t}
# which effectively makes them syntax sugar

# the associated keywords are "translated" as follows:
#   ref x -> x
#   copy x -> x.value
#   eval x -> [execution]
# but are still kept as op keywords

code = """
^Type Point = Type
{
    &Double x
    &Double y
    
    ^Function new = &Point(&Int x, &Int y)
    {
        return Point
        {
            x
            y
        }
    }
    
    ^Function diff = &Double(*Point self, *Point other)
    {
        return self.x - other.x + self.y - other.y
    }
}

*Point p1 = Point.new(10, 5)
&Point p2 = Point.new(3, 2)

&Double d = p1.diff(p2)
&Double x1 = p1.x
p1.y = p2.x
p2.y = x1
"""


class Compiler(Translator[str, abstract.Node]):
    def __init__(self):
        self.translators = (
            Evaluator(),
        )

    def translate(self, source):
        step = source
        for translator in self.translators:
            step = translator.translate(step)
        return step


def main():
    grammar.utils.regenerate()

    result = Compiler().translate(code)

    print(result.syntax())


if __name__ == "__main__":
    main()
