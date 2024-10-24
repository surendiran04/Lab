%{
#include "y.tab.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
%}

%%
"if"                  { return IF; }
"goto"                { return GOTO; }
[a-zA-Z][a-zA-Z0-9]*  { yylval.str = strdup(yytext); return ID; }  // Handle identifiers
[0-9]+                { yylval.str = strdup(yytext); return NUM; } // Handle numbers
"="                   { return ASSIGN; }
"+"                   { return ADD; }
"*"                   { return MUL; }
"-"                   { return SUB; }
"<"                   { return LT; }
":"                   { return COLON; }
\n                    { return NEWLINE; }
[ \t]+                { /* Ignore whitespaces */ }
<<EOF>>               { return END; }  // Handle end of file
.                     { /* Ignore unrecognized characters */ }

%%

int yywrap() {
    return 1;
}
