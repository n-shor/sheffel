grammar Grammar;

prog: SPACE* (block | stat)* SPACE* EOF;

block: SPACE* '{' ('\n' | SPACE)* (stat | block)* expr* (SPACE | '\n')* '}' (SPACE | '\n')*;

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
|  (behaviorQualifier SPACE+)? (type memoryQualifier)? SPACE*
       '(' (SPACE* expr SPACE* ',')* SPACE* expr SPACE* ')' (SPACE | '\n')* block    # FuncLiteral

|  VAR SPACE* '(' (SPACE* expr SPACE* ',')* SPACE* expr SPACE* ')'           # FuncCall
|  VAR                                               # Var
|  INT                                               # Int
|  FLOAT                                             # Float
|  '(' SPACE* expr SPACE* ')'                  # Parenthesize
;

// Lexer rules
CUSTOM_OP: [!#$%&*+-/:;<=>?@^|~]+ ; //problematic, might match default operators
INT: [0-9]+ ;
FLOAT: [0-9]* '.' [0-9]+ ;
VAR: [a-zA-Z_][a-zA-Z_0-9]* ;
SPACE: [ \t] ;
FULL_SKIP: [\r]+ -> skip ;  // Skips carriage returns
