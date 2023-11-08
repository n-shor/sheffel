set "build_dir=x64"
set "input_file=input.shf"

copy "./common.hpp" "%build_dir%/common.hpp"
bison -o "%build_dir%/parser.cpp" -d "./parser.y"
flex -o "%build_dir%/lex.yy.cc" "./lexer.l"

g++ "%build_dir%/parser.cpp" "%build_dir%/lex.yy.cc" -o "%build_dir%/parser" -static-libgcc -static-libstdc++ -static

start "" ./%build_dir%/parser.exe %input_file%