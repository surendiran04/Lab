%{

#include "y.tab.h"

%}



%%



[0-9]+  { yylval.str = strdup(yytext); return NUMBER; }  // Capture numbers as strings

"+"     { return PLUS; }

"-"     { return MINUS; }

"*"     { return TIMES; }

"/"     { return DIVIDE; }

\n      { return '\n'; }

[ \t]   { /* skip whitespaces */ }



%%



int yywrap() {

    return 1;

}
