import subprocess

from .ast import Block
from llvmlite.ir import Module


def run_from_exe(name: str,
                 run: bool = True,
                 print_result: bool = False,
                 **kwargs):
    if not run:
        return name

    result = subprocess.call([name])

    if print_result:
        print(result)

    return result


def compile_from_ir(*ir: Module,
                    exe: bool = True,
                    name: str = "program",
                    **kwargs):
    if not exe:
        return ir

    from .build.create import create_exe
    result = create_exe(*ir, name=name)

    return run_from_exe(result, **kwargs)


def compile_from_ast(ast: Block, *,
                     ir: bool = True,
                     print_ir: bool = False,
                     **kwargs):
    if not ir:
        return ast

    from .ir_generate.create import create_ir
    result = create_ir(ast)

    if print_ir:
        lines = str(result[0]).split('\n')
        lines_without_meta = lines[3:]
        print('\n'.join(lines_without_meta))

    return compile_from_ir(*result, **kwargs)


def compile_from_code(code: str, *,
                      ast: bool = True,
                      regenerate_grammar: bool = False, print_ast: bool = False,
                      **kwargs):
    if not ast:
        return code

    if regenerate_grammar:
        result = subprocess.call([
            'java',
            '-jar', './compiler/lex_parse/antlr-4.13.1-complete.jar',
            '-Dlanguage=Python3', './compiler/lex_parse/Grammar.g4',
            '-o', './compiler/lex_parse/grammar'
        ])

        if result == 0:
            print('Grammar regenerated successfully.')

        else:
            raise RuntimeError(f'Grammar regeneration process returned with a non-zero result {result}.')

    else:
        print('Warning: recompiling without regenerating grammar.')

    from .lex_parse.create import create_ast
    result = create_ast(code + '\n')

    if print_ast:
        from .ast import print_ast as print_
        print_(result)

    return compile_from_ast(result, **kwargs)


def compile_from_file(input_path: str, *,
                      code: bool = True,
                      **kwargs):
    if not code:
        return input_path

    with open(input_path, 'r') as f:
        result = f.read()

    return compile_from_code(result, **kwargs)
