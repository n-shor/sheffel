set "build_dir=./x64"
set "source_dir=."
set "input_file=./input.shf"


if not exist "%build_dir%" mkdir "%build_dir%"

copy "%source_dir%/common.hpp" "%build_dir%/common.hpp"
bison -o "%build_dir%/parser.cpp" -d "%source_dir%/parser.y"
flex -o "%build_dir%/lex.yy.cc" "%source_dir%/lexer.l"

g++ "%build_dir%/parser.cpp" "%build_dir%/lex.yy.cc" -o "%build_dir%/parser" -static-libgcc -static-libstdc++ -static

start "" %build_dir%/parser.exe %input_file%

python "%source_dir%/ir_generator.py"