import subprocess
import os

from llvmlite import ir, binding

from .file_constants import *


def create_exe(module: ir.Module):
    module.name = "module"
    module.triple = "x86_64-unknown-linux-gnu"
    module.data_layout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"

    if not os.path.isdir(BUILD_PATH):
        os.makedirs(BUILD_PATH)

    with open(f"{BUILD_PATH}/{IR_FILE}", 'w') as f:
        f.write(str(module))

    result = -1

    try:
        result = _mingw64_compilation_step(
            'llc',
            f'"{BUILD_PATH}/{IR_FILE}"',
            '-o', f'"{BUILD_PATH}/{ASM_FILE}"',
            name="Assembly file generation")

        result = _mingw64_compilation_step(
            'gcc',
            '-c', f'"{BUILD_PATH}/{ASM_FILE}"',
            '-o', f'"{BUILD_PATH}/{OBJECT_FILE}"',
            name="Object file generation")

        result = _mingw64_compilation_step(
            'gcc',
            f'"{BUILD_PATH}/{OBJECT_FILE}"',
            '-o', f'"{BUILD_PATH}/{EXECUTABLE_FILE}"',
            name="Executable file generation")

    except RuntimeError:
        return result

    return result


def _mingw64_compilation_step(*args: str, name: str):
    result = subprocess.call(['mingw64', *args])

    if result != 0:
        raise RuntimeError(f'{name} process returned with a non-zero result {result}.')

    print(f'{name} successful.')
    return result
