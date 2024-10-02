%option noyywrap

%{
#include<stdio.h>
#include<stdlib.h>
#include "y.tab.h"
%}

alpha   [A-Za-z]
digit   [0-9]

%%

[ \t\n]                          { /* Ignore whitespaces */ }

for                              { return FOR; }
{digit}+                         { yylval.str = strdup(yytext); return NUM; }
{alpha}({alpha}|{digit})*         { yylval.str = strdup(yytext); return ID; }
"<="                              { return LE; }
">="                              { return GE; }
"=="                              { return EQ; }
"!="                              { return NE; }
"||"                              { return OR; }
"&&"                              { return AND; }
.                                 { return yytext[0]; }

%%

