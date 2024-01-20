from .ast import Block, print_ast
from .lex_parse.create import create_ast
from .ir_generate.create import create_ir
from .bind.make import make_executable


def compile_file(input_file_path: str, *,
                 alternative_code: str = None,
                 print_generated_ast: bool = False,
                 alternative_ast: Block = None,
                 run_ir_generator: bool = True,
                 make_exe: bool = True):
    """Compiles the given input file. May also replace certain compilation steps with given inputs."""

    if alternative_code is None:
        with open(input_file_path, 'r') as f:
            code = f.read()
    else:
        code = alternative_code

    if alternative_ast is None:
        tree = create_ast(code)

        if print_generated_ast:
            print_ast(tree)
    else:
        tree = alternative_ast

    if make_exe and not run_ir_generator:
        print('Warning: remaking without regenerating IR. This will result in no compilation.')

    if run_ir_generator:
        module = create_ir(tree)
        if make_exe:
            make_executable(module)
