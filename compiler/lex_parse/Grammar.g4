grammar Grammar;

prog: stat+;

// Parser rules

stat:
   SPACE? '\n'                             # EmptyLine
|  SPACE? expr SPACE? '\n'                         # ExpressionLine
;

memory_qualifier: '*' | '&';
type_: 'Int' | 'Float';
behavior_qualifier: 'noread' | 'nowrite';

expr:
   expr SPACE? op=('*' | '/') SPACE? expr            # MulDiv
|  expr SPACE? op=('+' | '-') SPACE? expr            # AddSub
|  expr SPACE? op=CUSTOM_OP SPACE? expr              # CustomOperator
|  expr SPACE? op='=' SPACE? expr                    # Assignment
|  (behavior_qualifier SPACE)? type_ SPACE? memory_qualifier VAR               # Declaration
|  VAR                                             # Var
|  INT                                             # Int
|  FLOAT                                           # Float
|  LPAREN SPACE? expr SPACE? RPAREN                  # Parenthesize
;

// Lexer rules
LPAREN : '(' ;
RPAREN : ')' ;
CUSTOM_OP: [!#$%&*+-/:;<=>?@^|~]+ ;
INT: [0-9]+ ;
FLOAT: [0-9]* '.' [0-9]+ ;
VAR: [a-zA-Z_][a-zA-Z_0-9]* ;
SPACE: [ \t]+ ;
FULL_SKIP: [\r]+ -> skip ;  // Skips carriage returns
