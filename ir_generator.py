import json

BUILD_DIR = "./x64"

with open(f"{BUILD_DIR}/AST.json") as f:
    AST = json.loads(f.read())

PROGRAM = r"""
@formatString = private constant [13 x i8] c"Hello, World!\0A\00"

declare i32 @printf(i8*, ...)

define i32 @main() {
  call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([13 x i8], [13 x i8]* @formatString, i32 0, i32 0))
  ret i32 0
}
"""

with open(f"{BUILD_DIR}/IRCODE.ll", "w") as f:
    f.write(PROGRAM)