bison -o parser.cpp -d parser.y
flex -o lex.yy.cc lexer.l
g++ parser.cpp lex.yy.cc -o parser -static-libgcc -static-libstdc++ -static
