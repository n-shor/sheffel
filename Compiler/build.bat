bison -o parser.cpp -d parser.y
flex -o lexer.c lexer.l
echo "g++ parser.cpp lex.yy.cc -o parser -static-libgcc -static-libstdc++ -static"
