%{
#include "common.hpp"
#include "parser.hpp"
%}

%%

[0-9]+  { yylval.val = atoi(yytext); return NUMBER; }
[ \t]   { /* ignore whitespace */ }
"+"     { return '+'; }
"-"     { return '-'; }
"*"     { return '*'; }
\n      { /* ignore new lines */ }
.       { /* ignore everything else */ }

%%

int yywrap() {
  return 1;
}
