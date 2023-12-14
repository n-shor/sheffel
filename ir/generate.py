import os

from .env_constants import *

def generate(ast):
    
    with open(f'{BUILD_PATH}/{IR_FILE}', 'w') as f:
        f.write(...)

if not os.path.isdir(BUILD_PATH):
    os.makedirs(BUILD_PATH)