import subprocess
import os

from llvmlite import ir, binding


BUILD_DIR = "build_files"


def create_exe(module: ir.Module, name: str = 'Program'):
    module.name = name
    module.triple = "x86_64-unknown-linux-gnu"
    module.data_layout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"

    if not os.path.isdir(BUILD_DIR):
        os.makedirs(BUILD_DIR)

    ir_file_path = f'"{BUILD_DIR}/{name}.ll"'
    exe_file_path = f'"{BUILD_DIR}/{name}.exe"'

    with open(ir_file_path, 'w') as f:
        f.write(str(module))

    return subprocess.call(['clang', ir_file_path, '-o', exe_file_path])
