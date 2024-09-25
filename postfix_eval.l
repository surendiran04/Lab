%{

#include "y.tab.h"

%}



%%



[0-9]+  { yylval.num = atoi(yytext); return NUMBER; }  // Convert the string to an integer

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
