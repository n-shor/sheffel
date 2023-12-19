grammar Calc;
prog: expr;

// Parser rules

expr:
  expr op=('*' | '/') expr # MulDiv
| expr op=('+' | '-') expr # AddSub
| INT # Int
| FLOAT # Float
| LPAREN expr RPAREN # Factor
;


// Lexer rules
LPAREN : '(' ;
RPAREN : ')' ;
INT    : [0-9]+ ;
FLOAT  : [0-9]+ ('.' [0-9]+)? ; 
WS     : [ \t\r\n]+ -> skip ;
