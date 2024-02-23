from . import Node


def print_ast(node: Node, indent='  '):

    out = ""
    level = 0

    for c in repr(node):
        match c:
            case '(':
                level += 1
                out += '(\n' + level * indent

            case ')':
                level -= 1
                out += '\n' + level * indent + ')'

            case ',':
                out += ',' + ('\n' + level * indent if out[-1] != ')' else '')

            case _:
                out += c

    print(out)
