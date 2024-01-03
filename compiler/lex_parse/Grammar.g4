grammar Grammar;

prog: stat+;

// Parser rules

stat:
   OPT_S '\n'                              # EmptyLine
|  expr OPT_S '\n'                         # ExpressionLine
;

memory_qualifier: '*' | '&';
type_: 'Int' | 'Float';
behavior_qualifier: 'noread' | 'nowrite';

expr:
   (behavior_qualifier MAN_S)? type_ OPT_S memory_qualifier expr # Declaration
|  expr OPT_S op=('*' | '/') OPT_S expr            # MulDiv
|  expr OPT_S op=('+' | '-') OPT_S expr            # AddSub
|  expr OPT_S op=CUSTOM_OP OPT_S expr              # CustomOperator
|  expr OPT_S op='=' OPT_S expr                    # Assignment
|  INT                                             # Int
|  FLOAT                                           # Float
|  VAR                                             # Var
|  LPAREN OPT_S expr OPT_S RPAREN                  # Parenthesize
;

// Lexer rules
LPAREN : '(' ;
RPAREN : ')' ;
CUSTOM_OP: [!#$%&*+-/:;<=>?@^|~]+ ;
INT: [0-9]+ ;
FLOAT: [0-9]+ ('.' [0-9]+)? ;
VAR: [a-zA-Z]+ ;
MAN_S: [ \t]+ ;
OPT_S: [ \t]* ;
FULL_SKIP: [\r]+ -> skip ;  // Skips carriage returns
