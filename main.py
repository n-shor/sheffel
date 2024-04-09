from compiler.structure import grammar, abstract
from compiler.translate import Parser, ModuleAssembler

# TODO: register args | general: type constraints, and how to pass types to functions?
# NOTE: currently only eval-variables are scoped into a function.

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
&Int b = 4 + a + 43
&Double c = 5.6 + a
&Double d = b + c
"""


def compile_(source):
    prog = Parser().translate(source)
    prog = ModuleAssembler().translate(prog)
    return prog


def main():
    # grammar.utils.regenerate()

    print(compile_(code_2))


if __name__ == "__main__":
    main()
