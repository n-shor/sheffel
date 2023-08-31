bison -o parser.cpp -d parser.y
flex -o lex.yy.cc lexer.lex
g++ parser.cpp lex.yy.cc -o parser