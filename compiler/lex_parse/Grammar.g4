grammar Grammar;

prog: stat+;

// Parser rules

stat:
   OPT_S? '\n'                              # EmptyLine
|  OPT_S expr OPT_S '\n'                         # ExpressionLine
;

memory_qualifier: '*' | '&';
type_: 'Int' | 'Float';
behavior_qualifier: 'noread' | 'nowrite';

expr:
   expr OPT_S op=('*' | '/') OPT_S expr            # MulDiv
|  expr OPT_S op=('+' | '-') OPT_S expr            # AddSub
|  expr OPT_S op=CUSTOM_OP OPT_S expr              # CustomOperator
|  expr OPT_S op='=' OPT_S expr                    # Assignment
|  (behavior_qualifier MAN_S)? type_ OPT_S memory_qualifier VAR               # Declaration
|  VAR                                             # Var
|  INT                                             # Int
|  FLOAT                                           # Float
|  LPAREN OPT_S expr OPT_S RPAREN                  # Parenthesize
;

// Lexer rules
LPAREN : '(' ;
RPAREN : ')' ;
CUSTOM_OP: [!#$%&*+-/:;<=>?@^|~]+ ;
INT: [0-9]+ ;
FLOAT: [0-9]* '.' [0-9]+ ;
VAR: [a-zA-Z_][a-zA-Z_0-9]* ;
MAN_S: [ \t]+ ;
OPT_S: [ \t]* ;
FULL_SKIP: [\r]+ -> skip ;  // Skips carriage returns
