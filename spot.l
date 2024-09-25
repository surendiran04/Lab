%option noyywrap
%{
#include "y.tab.h"
#include <stdio.h>
#include <stdlib.h>
extern int yylval;
%}
%%
"switch"       { return SWITCH; }
"case"         { return CASE; }
"default"      { return DEFAULT; }
"break"        { return BREAK; }
":"            { return COLON; }
";"            { return SEMICOLON; }
"{"            { return LBRACE; }
"}"            { return RBRACE; }                                                                                              
[0-9]+         { yylval = atoi(yytext); return NUM; }
[a-zA-Z][a-zA-Z0-9]* { return IDENTIFIER; }
[ \t\n]+       ;
.              { return yytext[0]; }
%% 
