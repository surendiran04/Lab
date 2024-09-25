%{

#include "y.tab.h"

#include <string.h>

%}



%%



[0-9]+  { yylval.str = strdup(yytext); return NUMBER; }  // Use yylval.str for strings

"+"     { return PLUS; }

"-"     { return MINUS; }

"*"     { return TIMES; }

"/"     { return DIVIDE; }

"("     { return LPAREN; }

")"     { return RPAREN; }

\n      { return '\n'; }

[ \t]   { /* skip whitespaces */ }



%%



int yywrap() {

    return 1;

}
