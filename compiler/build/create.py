import subprocess
import os

from llvmlite import ir, binding


BUILD_DIR = "build_files"


def create_exe(module: ir.Module, name: str):
    """Compiles the .ll file. Returns the executable's full path."""

    module.name = name

    if not os.path.isdir(BUILD_DIR):
        os.makedirs(BUILD_DIR)

    build_dir_path = f'{os.getcwd()}\\{BUILD_DIR}'
    ir_file_path = f'{build_dir_path}\\{name}.ll'
    exe_file_path = f'{build_dir_path}\\{name}.exe'

    with open(ir_file_path, 'w') as f:
        f.write(str(module))

    result = subprocess.call(['clang', ir_file_path, '-o', exe_file_path, '-Wno-override-module'])

    if result != 0:
        raise RuntimeError(f"Compilation returned with a non-zero result {result}.")

    print("Compilation successful.")
    return exe_file_path
