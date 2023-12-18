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
    | FLOAT                  # Float
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
FLOAT: [0-9]+ ('.' [0-9]+)? ;
NEWLINE:'\r'? '\n';
WS: [ \t]+ -> skip;