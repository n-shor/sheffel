grammar Grammar;

prog:
    stat* SPACE* EOF
;

stat:
    SPACE* '\n'             # EmptyStat
|   expr '\n'               # ExpressionStat
|   block '\n'              # BlockStat
;

block:
    '{\n' stat* '}'         # MultiLineBlock
|   '{' expr '}'            # SingleLineBlock
;

memoryQualifier: '*' | '&';
typeName: 'Int' | 'Long' | 'Float' | 'Double' | 'Function';
behaviorQualifier: 'noread' | 'nowrite';

variableType:
    (behaviorQualifier SPACE+)* typeName memoryQualifier    # FullVariableType
|   (behaviorQualifier SPACE+)* memoryQualifier             # AutoVariableType
;

expr:
    SPACE+ expr                                         # LeftSpacedExpr
|   expr SPACE+                                         # RightSpacedExpr
|   '(' expr ')'                                        # ParenthesizedExpr

|   expr op=OP expr                                     # BinaryOperatorExpr
|   expr SPACE* '(' ((expr ',')* expr)? ')'             # CallOperatorExpr

|   variableType SPACE+ name=VAR                        # VariableDeclarationExpr

|   variableType SPACE* '(' ((expr ',')* expr)? ')' (SPACE | '\n')* block   # FunctionCreationExpr
|   '(' ((expr ',')* expr)? ')' (SPACE | '\n')* block                       # VoidReturningFunctionCreationExpr

|   'copy' SPACE+ expr                                  # CopyExpr
|   'view' SPACE+ expr                                  # ViewExpr
|   'return' SPACE+ expr?                               # ReturnExpr

|   name=VAR                                            # VarExpr
|   value=INT                                           # IntExpr
|   value=DOUBLE                                        # DoubleExpr
;


// Lexer rules

FULL_SKIP: [\r]+ -> skip ;
SPACE: [ \t] ;

INT: [0-9]+ ;
DOUBLE: [0-9]* '.' [0-9]+ ;
VAR: [a-zA-Z_][a-zA-Z_0-9]* ;

OP: [!#$%&*+-/:;<=>?@^|~]+ ;
