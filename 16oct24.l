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

/* Assignment operator */
"="         { return ASSIGN; }

/* Arithmetic operators */
"+"         { return '+'; }
"-"         { return '-'; }
""         { return ''; }
"/"         { return '/'; }

/* Brackets and parentheses */
"("         { return LPAR; }
")"         { return RPAR; }
"{"         { return LBRACE; }
"}"         { return RBRACE; }
"["         { return LBRACKET; }
"]"         { return RBRACKET; }

/* Numbers */
[0-9]+      { yylval = strdup(yytext); return NUM; }

/* Identifiers (variables, array names) */
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
    return 1;
}
