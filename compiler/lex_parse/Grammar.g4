grammar Grammar;

prog:
    stat* SPACE* EOF
;

stat:
    SPACE* '\n'                                         # EmptyStat
|   SPACE* expr '\n' (SPACE | '\n')*                    # ExpressionStat
|   SPACE* block '\n' (SPACE | '\n')*                   # BlockStat
|   SPACE* 'return' (SPACE+ expr)? (SPACE | '\n')*      # ReturnStat
;

block:
    '{' SPACE* '\n'? stat* SPACE* '}'                         # MultiLineBlock
|   '{' expr '}'                                # SingleLineBlock
|   'while' SPACE+ expr (SPACE | '\n')*
    block (SPACE | '\n')*                       # WhileBlock
|   'if' SPACE+ expr (SPACE | '\n')*
    block (SPACE | '\n')*
    ('else' (SPACE | '\n')* block (SPACE | '\n')*)?      # IfBlock
;

memoryQualifier: '*' | '&';
typeName: 'Int' | 'Long' | 'Float' | 'Double' | 'Function' | 'Bool';
behaviorQualifier: 'noread' | 'nowrite';

variableType:
    (behaviorQualifier SPACE+)* typeName memoryQualifier    # FullVariableType
|   (behaviorQualifier SPACE+)* memoryQualifier             # AutoVariableType
;

expr:
    SPACE+ expr             # LeftSpacedExpr
|   expr SPACE+             # RightSpacedExpr
|   '(' expr ')'            # ParenthesizedExpr

|   'copy' SPACE+ expr      # CopyExpr
|   'view' SPACE+ expr      # ViewExpr

|   expr SPACE* '(' ((expr ',')* expr)? ')'                 # CallOpExpr
|   op=OP expr                                              # UnaryOpExpr
|   expr op=('*' | '/') expr                                # MulDivOpExpr
|   expr op=('+' | '-') expr                                # AddSubOpExpr
|   expr op=('<' | '<=' | '>' | '>=' | '==' | '!=') expr    # CompareOpExpr
|   expr op='=' expr                                        # AssignOpExpr

|   variableType SPACE+ name=VAR                            # VariableDeclarationExpr

|   (variableType SPACE*)? '(' ((expr ',')* expr)? ')' (SPACE | '\n')* block    # FunctionCreationExpr

|   name=VAR        # VarExpr
|   value=INT       # IntExpr
|   value=LONG      # LongExpr
|   value=HEX       # HexExpr
|   value=BINARY    # BinaryExpr
|   value=DOUBLE    # DoubleExpr
|   value=FLOAT     # FloatExpr
|   value=BOOL      # BoolExpr
;


// Lexer rules

FULL_SKIP: [\r]+ -> skip ;
SPACE: [ \t] ;

INT: [0-9]+ ;
LONG: [0-9]+ [lL] ;
HEX: '0x' ([0-9] | [a-f] | [A-F])+ [lL]? ;
BINARY: [01]+ [bB] [lL]? ;
DOUBLE: [0-9]* '.' [0-9]+ ;
FLOAT: ([0-9]* '.')? [0-9]+ [fF] ;
BOOL: 'true' | 'false' ;
VAR: [a-zA-Z_][a-zA-Z_0-9]* ;

OP: [!#$%&*+-/:;<=>?@^|~]+ ;
