%{
#include "parser.tab.hpp"
extern int yylval;
%}

%%

[0-9]+ { yylval = atoi(yytext); return NUMBER; }
[ \t]  { /* ignore whitespace */ }
"+"    { return ADD; }
"-"    { return SUB; }
"*"    { return MUL; }
\n     { return EOL; }
.      { /* ignore everything else */ }

%%

int yywrap() {
  return 1;
}
