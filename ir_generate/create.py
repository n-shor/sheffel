import os

from .env_constants import *

from ..ast.nodes import Node
from llvm_translator import LLVMTranslator

RAW_HELLO_WORLD_PROGRAM = """; Copied directly from the documentation
; Declare the string constant as a global constant.
@.str = private unnamed_addr constant [14 x i8] c"hello world\0A\00"

; External declaration of the puts function
declare i32 @puts(i8* nocapture) nounwind

; Definition of main function
define i32 @main() { ; i32()*
    ; Convert [13 x i8]* to i8  *...
    %cast210 = getelementptr [13 x i8],[13 x i8]* @.str, i64 0, i64 0

    ; Call puts function to write out the string to stdout.
    call i32 @puts(i8* %cast210)
    ret i32 0
}

; Named metadata
!0 = !{i32 42, null, !"string"}
!foo = !{!0}"""

def create_ir(ast: list[Node]):
    """Creates an IR file from the AST."""
    
    translator = LLVMTranslator()
    translator.generate(ast)
    
    with open(f'{BUILD_PATH}/{IR_FILE}', 'w') as f:
        f.write(translator.get_ir())

if not os.path.isdir(BUILD_PATH):
    os.makedirs(BUILD_PATH)