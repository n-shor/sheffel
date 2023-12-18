grammar calc;

prog: expr;

/*********/
/*       */
/* rules */
/*       */
/*********/
expr: expr op=('*'|'/') expr # MulDiv
    | expr op=('+'|'-') expr # AddSub
    | '(' expr ')'           # Paren
    | INT                    # Int
    | STR                    # Str
    ;

/**********/
/*        */
/* tokens */
/*        */
/**********/
ADD: '+' ;
MUL: '*' ;
DIV: '/' ;
SUB: '-' ;
STR: [a-zA-Z]+ ;
INT: [0-9]+ ;
NEWLINE:'\r'? '\n';
WS: [ \t]+ -> skip;