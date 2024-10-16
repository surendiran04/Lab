%{
#include "y.tab.h"
%}

%%

/* Keywords */
"for"       { return FOR; }
"while"     { return WHILE; }
"if"        { return IF; }
"else"      { return ELSE; }

/* Relational operators */
"<="        { return LE; }
">="        { return GE; }
"=="        { return EQ; }
"!="        { return NE; }
"<"         { return LT; }
">"         { return GT; }

/* Logical operators */
"&&"        { return AND; }
"||"        { return OR; }

/* Assignment operator */
"="         { return ASSIGN; }

/* Arithmetic operators */
"+"         { return '+'; }
"-"         { return '-'; }
""         { return ''; }
"/"         { return '/'; }

/* Parentheses and braces */
"("         { return LPAR; }
")"         { return RPAR; }
"{"         { return LBRACE; }
"}"         { return RBRACE; }

/* Semicolon */
";"         { return ';'; }

/* Numbers */
[0-9]+      { yylval = strdup(yytext); return NUM; }

/* Identifiers */
[a-zA-Z_][a-zA-Z0-9_]* {
    yylval = strdup(yytext);
    return ID;
}

/* Whitespace and newlines */
[ \t\n]+    /* Ignore whitespace */

/* Any other character */
.           { printf("Unexpected character: %s\n", yytext); }

%%

int yywrap() {
    return 1;
}
