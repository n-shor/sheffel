grammar Grammar;

prog: stat+;

// Parser rules

stat:
   '\n'                              # EmptyLine
|  expr '\n'                         # ExpressionLine
|  (behavior_qualifier)? (type_qualifier)(memory_qualifier) VAR '=' expr '\n'   # AssignmentDeclarationLine
|  (behavior_qualifier)? (type_qualifier)(memory_qualifier) VAR '\n'            # DeclarationLine
|  VAR '=' expr '\n'                                                            # VariableAssignmentLine
|  '{' expr '}'                                                                 # SingleLineScope
//|  expr '=' expr '\n'                                                           # AssignmentLine
;

memory_qualifier: '*' | '&';
type_qualifier: 'Int' | 'Float';
behavior_qualifier: 'noread' | 'nowrite';

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
