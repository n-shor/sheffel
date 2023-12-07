grammar Calc;

// Parser rules
expr   : term ((PLUS | MINUS) term)* ;
term   : factor ((MUL | DIV) factor)* ;
factor : INT | LPAREN expr RPAREN ;

// Lexer rules
WS      : [ \t\r\n]+ -> skip ;
INT     : [0-9]+ ;
PLUS    : '+' ;
MINUS   : '-' ;
MUL     : '*' ;
DIV     : '/' ;
LPAREN  : '(' ;
RPAREN  : ')' ;
