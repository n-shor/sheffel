grammar Calc;

prog: stat+;

// Parser rules

stat:
   '\n'                              # EmptyLine
|  expr '\n'                         # ExpressionLine
|  (dataType)? VAR '=' expr '\n'        # AssignmentLine
|  (dataType)? VAR '\n'                 # DeclarationLine
;

dataType: 'Int' | 'Float';

expr:
   expr op=('*' | '/') expr            # MulDiv
|  expr op=('+' | '-') expr            # AddSub
|  INT                                 # Int
|  FLOAT                               # Float
|  VAR                                 # Var
|  LPAREN expr RPAREN                  # Factor
;

// Lexer rules
LPAREN : '(' ;
RPAREN : ')' ;
INT: [0-9]+;
FLOAT: [0-9]+ ('.' [0-9]+)?;
VAR: [a-zA-Z]+;
WS : [ \t\r]+ -> skip ;  // Skips whitespace and carriage returns