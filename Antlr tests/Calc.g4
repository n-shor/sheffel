grammar Calc;
prog: exper;

// Parser rules

exper:
| exper op=('*' | '/') exper 
| exper op=('+' | '-') exper 
| '(' exper ')' # Factor
| INT # Int
| FLOAT # Float
;


// Lexer rules
INT    : [0-9]+ ;
FLOAT  : [0-9]+ ('.' [0-9]+)? ; 
WS     : [ \t\r\n]+ -> skip ;
