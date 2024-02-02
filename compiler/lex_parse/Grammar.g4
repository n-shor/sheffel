grammar Grammar;

prog:
    stat* SPACE* EOF
;

stat:
    SPACE* '\n'                  # EmptyStat
|   expr '\n' (SPACE | '\n')*    # ExpressionStat
|   block '\n' (SPACE | '\n')*   # BlockStat
;

block:
    '{' '\n'? stat* '}'         # MultiLineBlock
|   '{' expr '}'            # SingleLineBlock
|   'if' SPACE+ expr (SPACE | '\n')* block (SPACE | '\n')*
    ('else' SPACE+ block (SPACE | '\n')*)? # IfBlock
;

memoryQualifier: '*' | '&';
typeName: 'Int' | 'Long' | 'Float' | 'Double' | 'Function' | 'Bool';
behaviorQualifier: 'noread' | 'nowrite';

variableType:
    (behaviorQualifier SPACE+)* typeName memoryQualifier    # FullVariableType
|   (behaviorQualifier SPACE+)* memoryQualifier             # AutoVariableType
;

expr:
    SPACE+ expr                                         # LeftSpacedExpr
|   expr SPACE+                                         # RightSpacedExpr
|   '(' expr ')'                                        # ParenthesizedExpr

|   name=VAR                                            # VarExpr
|   value=INT                                           # IntExpr
|   value=DOUBLE                                        # DoubleExpr
|   value=BOOL                                          # BoolExpr

|   expr SPACE* '(' ((expr ',')* expr)? ')'             # CallOpExpr
|   expr op=('*' | '/') expr                            # MulDivOpExpr
|   op=('+' | '-') expr                                 # UnarySignOpExpr
|   expr op=('+' | '-') expr                            # AddSubOpExpr
|   expr op='=' expr                                    # AssignOpExpr

|   variableType SPACE+ name=VAR                        # VariableDeclarationExpr

|   variableType SPACE* '(' ((expr ',')* expr)? ')' (SPACE | '\n')* block   # FunctionCreationExpr
|   '(' ((expr ',')* expr)? ')' (SPACE | '\n')* block                       # VoidReturningFunctionCreationExpr

|   'copy' SPACE+ expr                                  # CopyExpr
|   'view' SPACE+ expr                                  # ViewExpr
|   'return' SPACE+ expr?                               # ReturnExpr
;


// Lexer rules

FULL_SKIP: [\r]+ -> skip ;
SPACE: [ \t] ;

INT: [0-9]+ ;
DOUBLE: [0-9]* '.' [0-9]+ ;
BOOL: 'true' | 'false' ;
VAR: [a-zA-Z_][a-zA-Z_0-9]* ;

OP: [!#$%&*+-/:;<=>?@^|~]+ ;
