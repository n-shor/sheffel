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

    subprocess.run(f'mingw64 llc "{BUILD_PATH}/{IR_FILE}" -o "{BUILD_PATH}/{ASM_FILE}"')
    subprocess.run(f'mingw64 gcc -c "{BUILD_PATH}/{ASM_FILE}" -o "{BUILD_PATH}/{OBJECT_FILE}"')
    subprocess.run(f'mingw64 gcc "{BUILD_PATH}/{OBJECT_FILE}" -o "{BUILD_PATH}/{EXECUTABLE_FILE}"')

    return 0
