%{
#include "y.tab.h"
%}

letter      [a-zA-Z]
digit       [0-9]
identifier  {letter}({letter}|{digit})*

%%

"int"       { return INT; }
"float"     { return FLOAT; }
"char"      { return CHAR; }
"double"    { return DOUBLE; }
{identifier} { yylval.str = strdup(yytext); return IDENTIFIER; }
";"         { return SEMICOLON; }
[ \t\n]     { /* ignore whitespace */ }

%%

int yywrap() {
    return 1;
}

