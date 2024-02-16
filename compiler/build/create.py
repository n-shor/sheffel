import subprocess
import os

from llvmlite import ir, binding


BUILD_DIR = "build_files"


def create_exe(main_module: ir.Module, *dependencies: ir.Module, name: str):
    """Compiles the .ll file. Returns the executable's full path."""

    main_module.name = name

    if not os.path.isdir(BUILD_DIR):
        os.makedirs(BUILD_DIR)

    ir_file_paths = []

    for m in (main_module, *dependencies):

        path = f'{BUILD_DIR}\\{m.name}.ll'

        with open(path, 'w') as f:
            f.write(str(m))

        ir_file_paths.append(path)

    exe_file_path = f'{BUILD_DIR}\\{name}.exe'

    result = subprocess.call(['clang', *ir_file_paths, '-o', exe_file_path, '-Wno-override-module'])

    if result != 0:
        raise RuntimeError(f"Compilation returned with a non-zero result {result}.")

    print("Compilation successful.")
    return exe_file_path
