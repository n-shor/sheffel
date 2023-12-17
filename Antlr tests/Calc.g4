grammar Calc;
prog: exper;

// Parser rules

exper: exper op=('*' | '/') exper #MulDev
| exper op=('-' | '+') exper #AddSub
| INT # Int
| FLOAT # Float
;


// Lexer rules
INT    : [0-9]+ ;
FLOAT  : [0-9]+ ('.' [0-9]+)? ; 
WS     : [ \t\r\n]+ -> skip ;
