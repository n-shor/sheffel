grammar Grammar;

prog
:   NL? stat* EOF?
;

stat
:   expr NL             # ExpressionStat
|   block NL            # BlockStat
|   'return' expr? NL   # ReturnStat
;

block
:   '{' expr '}'                                    # SingleLineBlock
|   '{' NL stat* '}'                                # MultiLineBlock
|   'if' expr NL? block (NL? 'else' NL? block)?     # IfBlock
|   'while' expr NL? block                          # WhileBlock
;

expr
:   literal         # LiteralExpr

|   qualified=expr name=VAR     # DeclarationExpr
|   name=VAR                    # VarExpr

|   expr '(' ((expr ',')* expr)? ')'                        # CallOpExpr
|   op=OP expr                                              # UnaryOpExpr
|   expr op=('*' | '/' | '%') expr                          # MulDivModOpExpr
|   expr op=('+' | '-') expr                                # AddSubOpExpr
|   expr op=('<' | '<=' | '>' | '>=' | '==' | '!=') expr    # CompareOpExpr
|   expr '=' expr                                           # AssignOpExpr
;

literal
:   INT         # IntLiteral
|   DOUBLE      # DoubleLiteral
|   BOOL        # BoolLiteral
|   CHAR        # CharLiteral
|   STR         # StrLiteral

|   type_name=VAR memory=('^' | '&' | '*')                              # QualifiedLiteral
|   '(' ((args+=expr ',')* args+=expr)? ')' ret_type=expr? NL? block    # FunctionLiteral
|   '[' ((vals+=expr ',')* vals+=expr)? ']' elem_type=expr              # ArrayLiteral
;


NL: '\n'+ ;

INT:    [0-9]+ ;
DOUBLE: [0-9]* '.' [0-9]+ ;
BOOL:   'true' | 'false' ;
CHAR:   '\'' . '\'' ;
STR:    '"' .+? '"' ;

VAR:        [a-zA-Z_][a-zA-Z_0-9]* ;
OP:         [!#$%&*+-/:;<=>?@^|~]+ ;

INL_S:          [ \t]+ -> skip ;
CARRAGE_RETURN: [\r]+ -> skip ;
