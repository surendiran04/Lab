%{
#include "y.tab.h"
%}

%%

"<!--"                        { return COMMENT_START; }
"-->"                         { return COMMENT_END; }
"<"                           { return TAG_OPEN; }
"</"                          { return TAG_CLOSE; }
">"                           { return TAG_END; }
"/>"                          { return TAG_SELF_CLOSE; }
[a-zA-Z_:][a-zA-Z0-9_:.-]*    { yylval.str = strdup(yytext); return IDENTIFIER; }
\"[^\"]*\"                    { yylval.str = strdup(yytext); return ATTR_VALUE; }
"="                           { return EQUALS; }
"{"                           { return BRACE_OPEN; }
"}"                           { return BRACE_CLOSE; }
";"                           { return SEMICOLON; }
":"                           { return COLON; }
"/*"                          { return CSS_COMMENT_START; }
"*/"                          { return CSS_COMMENT_END; }
"[a-zA-Z][a-zA-Z0-9_-]*"      { yylval.str = strdup(yytext); return CSS_PROPERTY; }
"@media"                      { return MEDIA; }
"@import"                     { return IMPORT; }
"@"[a-zA-Z][a-zA-Z0-9_-]*     { yylval.str = strdup(yytext); return AT_RULE; }
"."[a-zA-Z][a-zA-Z0-9_-]*     { yylval.str = strdup(yytext); return CLASS_NAME; }
"#"[a-zA-Z][a-zA-Z0-9_-]*     { yylval.str = strdup(yytext); return ID_NAME; }
":"[a-zA-Z-]+                 { yylval.str = strdup(yytext); return PSEUDO_CLASS; }
[0-9]+                        { yylval.str = strdup(yytext); return NUMBER; }
[^<>{}]+                      { yylval.str = strdup(yytext); return TEXT; }

[ \t\n]+                      ;  // Ignore whitespace

%%

int yywrap() { return 1; }
