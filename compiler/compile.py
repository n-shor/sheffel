from .ast.nodes import *


def compile_file(input_file_path: str, *,
                 alternative_code: str = None, alternative_ast: list[Node] = None,
                 run_ir_generator: bool = True, make_executable: bool = True):
    """Compiles the given input file. May also replace certain compilation steps with given inputs."""

    if make_executable and not run_ir_generator:
        print('Warning: recompiling without regenerating IR.')

    if alternative_code is None:
        with open(input_file_path, 'r') as f:
            code = f.read()
    else:
        code = alternative_code

    if alternative_ast is None:
        from .lex_parse.create import create_ast
        tree = create_ast(code)
        print(recursive_dir(tree))
    else:
        tree = alternative_ast

    if run_ir_generator:
        from .ir_generate.create import create_ir
        create_ir(tree)

    if make_executable:
        from .ir_generate.make import make
        make()


def recursive_dir(x, /, padding=''):
    next_padding = padding + '\t'

    result = f'{padding}{type(x)}(\n'

    for attr_name in dir(x):
        if attr_name.startswith('__') and attr_name.endswith('__'):
            continue

        attr = getattr(x, attr_name)

        if isinstance(attr, Node):
            result += recursive_dir(attr, next_padding) + '\n'

        else:
            result += f'{next_padding}{attr}\n'

    result += f'{padding})'

    return result
