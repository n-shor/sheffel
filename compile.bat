mingw64.exe bison -o parser.cpp -d parser.y
mingw64.exe flex -o lex.yy.cc lexer.l

mingw64.exe g++ parser.cpp lex.yy.cc -o parser