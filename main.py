from compiler.structure import grammar, abstract
from compiler.translate import Parser, Resolver

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

code_1 = """
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

code_2 = """
^Int a = 13
&Int b = 4
&Double c = 5.6 + 7.8
^Double d = eval b + c
"""


def compile(source):
    abstract = Parser().translate(source)
    resolved = Resolver().translate(abstract)
    return resolved


def main():
    grammar.utils.regenerate()

    print(compile(code_2).syntax())


if __name__ == "__main__":
    main()
