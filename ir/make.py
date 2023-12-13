import subprocess

from .env_constants import *

def make():
    
    subprocess.run(
        f'mingw64 llc "{BUILD_PATH}/{IR_FILE}" -o "{BUILD_PATH}/{ASM_FILE}"',
        shell=True, check=True)
    
    subprocess.run(
        f'mingw64 gcc -c "{BUILD_PATH}/{ASM_FILE}" -o "{BUILD_PATH}/{OBJECT_FILE}"',
        shell=True, check=True)
    
    subprocess.run(
        f'mingw64 gcc "{BUILD_PATH}/{OBJECT_FILE}" -o "{BUILD_PATH}/{EXE_FILE}"',
        shell=True, check=True)
