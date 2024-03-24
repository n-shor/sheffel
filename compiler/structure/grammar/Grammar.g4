grammar Grammar;

prog
:   stat* EOF?
;

stat
:   NL                  # EmptyStat
|   expr NL             # ExpressionStat
|   block NL            # BlockStat
|   'return' expr? NL   # ReturnStat
;

block
:   '{' expr '}'                                    # SingleLineBlock
|   '{' NL? stat* '}'                               # MultiLineBlock
|   'if' expr NL? block (NL? 'else' NL? block)?     # IfBlock
|   'while' expr NL? block                          # WhileBlock
;

expr
:   INT         # IntLiteralExpr
|   DOUBLE      # DoubleLiteralExpr
|   BOOL        # BoolLiteralExpr
|   CHAR        # CharLiteralExpr
|   STR         # StrLiteralExpr

|   memory=('&' | '*' | '^') expr                          # MemoryCompositionExpr
|   expr '(' ((expr ',')* expr)? ')' NL? block  # FunctionCompositionExpr
|   expr '[' ((expr ',')* expr)? ']'            # ArrayCompositionExpr

|   name=VAR                # VariableExpr
|   expr name=VAR           # DeclarationExpr
|   expr '.' name=VAR       # AccessExpr

|   expr NL? block                                          # InitializeExpr
|   expr '(' ((expr ',')* expr)? ')'                        # CallExpr
|   expr '[' expr ']'                                       # IndexExpr

|   expr op=('*' | '/' | '%') expr                          # MulDivModExpr
|   expr op=('+' | '-') expr                                # AddSubExpr
|   expr op=('<' | '<=' | '>' | '>=' | '==' | '!=') expr    # CompareExpr
|   expr '=' expr                                           # AssignExpr

|   '(' expr ')'  # ParenthesizeExpr
;


NL: '\n'+ ;

INT:    [0-9]+ ;
DOUBLE: [0-9]* '.' [0-9]+ ;
BOOL:   'true' | 'false' ;
CHAR:   '\'' . '\'' ;
STR:    '"' .+? '"' ;

VAR:        [a-zA-Z_][a-zA-Z_0-9]* ;

INL_S:          [ \t]+ -> skip ;
CARRAGE_RETURN: [\r]+ -> skip ;
