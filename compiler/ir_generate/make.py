import subprocess

from .file_constants import *


def make():
    """Responsible for every compilation step beyond IR generation"""
    
    subprocess.run(f'mingw64 llc "{BUILD_PATH}/{IR_FILE}" -o "{BUILD_PATH}/{ASM_FILE}"')
    subprocess.run(f'mingw64 gcc -c "{BUILD_PATH}/{ASM_FILE}" -o "{BUILD_PATH}/{OBJECT_FILE}"')
    subprocess.run(f'mingw64 gcc "{BUILD_PATH}/{OBJECT_FILE}" -o "{BUILD_PATH}/{EXECUTABLE_FILE}"')
