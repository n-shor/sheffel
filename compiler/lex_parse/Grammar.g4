grammar Grammar;

prog: SPACE* (block | stat)* SPACE* EOF;

block: SPACE* '{' SPACE* (block | stat)* SPACE* '}' SPACE*;

// Parser rules

stat:
   SPACE* '\n'                             # EmptyLine
|  SPACE* expr SPACE* '\n'                         # ExpressionLine
;

memoryQualifier: '*' | '&';
type: 'Int' | 'Float' | 'Func';
behaviorQualifier: 'noread' | 'nowrite';

expr:
   expr SPACE* op=('*' | '/') SPACE* expr            # MulDiv
|  expr SPACE* op=('+' | '-') SPACE* expr            # AddSub
|  expr SPACE* op='=' SPACE* expr                    # Assignment
|  (behaviorQualifier SPACE+)? type memoryQualifier SPACE+ VAR               # Declaration
|  VAR                                               # Var
//|                                                  # FuncValue
|  INT                                               # Int
|  FLOAT                                             # Float
|  LPAREN SPACE* expr SPACE* RPAREN                  # Parenthesize
;

// Lexer rules
LPAREN : '(' ;
RPAREN : ')' ;
CUSTOM_OP: [!#$%&*+-/:;<=>?@^|~]+ ;
INT: [0-9]+ ;
FLOAT: [0-9]* '.' [0-9]+ ;
VAR: [a-zA-Z_][a-zA-Z_0-9]* ;
SPACE: [ \t] ;
FULL_SKIP: [\r]+ -> skip ;  // Skips carriage returns
