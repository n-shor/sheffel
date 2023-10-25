%{
#include "common.hpp"
#include "parser.hpp"
extern FILE *yyin;
%}

%%

[0-9]+  { yylval.val = atoi(yytext); return NUMBER; }
[ \t]   { /* ignore whitespace */ }
"+"     { return '+'; }
"-"     { return '-'; }
"*"     { return '*'; }
";"     { return ';'; }
.       { /* ignore everything else */ }

%%

int yywrap() {
  return 1;
}
