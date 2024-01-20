grammar Grammar;

prog: SPACE* (block | stat)* SPACE* EOF;

block: SPACE* '{' ('\n' | SPACE)* (stat | block)* ('\n' | SPACE)* '}' (SPACE | '\n')*;

// Parser rules

stat:
   SPACE* '\n'                             # EmptyLine
|  SPACE* expr SPACE* '\n'                         # ExpressionLine
;

memoryQualifier: '*' | '&';
type: 'Int' | 'Long' | 'Float' | 'Double' | 'Function';
behaviorQualifier: 'noread' | 'nowrite';

expr:
   expr SPACE* op=('*' | '/') SPACE* expr            # MulDiv
|  expr SPACE* op=('+' | '-') SPACE* expr            # AddSub
|  expr SPACE* op='=' SPACE* expr                    # Assignment
|  (behaviorQualifier SPACE+)? type memoryQualifier SPACE+ VAR               # Declaration
|  (behaviorQualifier SPACE+)? (type memoryQualifier)? SPACE*
       '(' (SPACE* expr SPACE* ',')* SPACE* expr SPACE* ')' (SPACE | '\n')* block    # FuncLiteral

|  expr SPACE* '(' (SPACE* expr SPACE* ',')* SPACE* expr SPACE* ')'           # FuncCall
|  VAR                                               # Var
|  INT                                               # Int
|  DOUBLE                                            # Double
|  '(' SPACE* expr SPACE* ')'                  # Parenthesize
|  'return' SPACE* expr                        # Return
;

// Lexer rules
CUSTOM_OP: [!#$%&*+-/:;<=>?@^|~]+ ; //problematic, might match default operators
INT: [0-9]+ ;
DOUBLE: [0-9]* '.' [0-9]+ ;
VAR: [a-zA-Z_][a-zA-Z_0-9]* ;
SPACE: [ \t] ;
FULL_SKIP: [\r]+ -> skip ;  // Skips carriage returns
