grammar Grammar;

prog:
    ONL_S? (stat RNL_S)* EOF
;

stat:
    expr                    # ExpressionStat
|   block                   # BlockStat
|   'return' (INL_S expr)?  # ReturnStat
;

block:
    '{' RNL_S (stat RNL_S)* '}'                               # MultiLineBlock
|   '{' expr '}'                                              # SingleLineBlock
|   'if' INL_S expr ONL_S block (ONL_S 'else' ONL_S block)?   # IfBlock
|   'while' INL_S expr ONL_S block                            # WhileBlock
;

memory:
    '^'     # EvalMemory
|   '&'     # CopyMemory
|   '*'     # RefMemory
;

expr:
    INL_S expr      # LeftSpacedExpr
|   expr INL_S      # RightSpacedExpr
|   '(' expr ')'    # ParenthesizedExpr

|   expr '(' ((expr ',')* expr)? ')'                        # CallOpExpr
|   op=OP expr                                              # UnaryOpExpr
|   expr op=('*' | '/' | '%') expr                          # MulDivModOpExpr
|   expr op=('+' | '-') expr                                # AddSubOpExpr
|   expr op=('<' | '<=' | '>' | '>=' | '==' | '!=') expr    # CompareOpExpr
|   expr op='=' expr                                        # AssignOpExpr

|   expr INL_S name=VAR     # DeclarationExpr
|   name=VAR                # VarExpr

|   type_name=VAR memory                            # QualifiedTypeExpr
|   expr '(' ((expr ',')* expr)? ')' ONL_S block    # ReturningFunctionExpr
|   '(' ((expr ',')* expr)? ')' ONL_S block         # VoidFunctionExpr
|   expr '[' ((expr ',')* expr)? ']'                # TypedArrayExpr
|   '[' (expr ',')* expr ']'                        # UntypedArrayExpr
|   value=INT       # IntExpr
|   value=LONG      # LongExpr
|   value=DOUBLE    # DoubleExpr
|   value=FLOAT     # FloatExpr
|   value=BOOL      # BoolExpr
|   value=CHAR      # CharExpr
|   value=STR       # StrExpr
;


FULL_SKIP:  [\r]+ -> skip ;
INL_S:      [ \t]+  ;
ONL_S:      [ \t\n]+ ;
RNL_S:      ONL_S? '\n' ONL_S? ;

VAR:        [a-zA-Z_][a-zA-Z_0-9]* ;
OP:         [!#$%&*+-/:;<=>?@^|~]+ ;

INTEGRAL:
    [0-9]
|   '0x' ([0-9] | [a-f] | [A-F])+
|   [01]+ [bB]
;

FLOATING:
    [0-9]* '.' [0-9]+
;

INT:    INTEGRAL ;
LONG:   INTEGRAL [lL];
DOUBLE: FLOATING | (INTEGRAL [dD]) ;
FLOAT:  FLOATING | INTEGRAL [fF] ;
BOOL:   'true' | 'false' ;
CHAR:   '\'' . '\'' ;
STR:    '"' .+? '"' ;
