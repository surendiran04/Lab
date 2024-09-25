%{

#include <stdio.h>

#include <stdlib.h>

#include <string.h>

#include <ctype.h>



void yyerror(const char *s);

int yylex();

char* concat(const char *s1, const char *s2);

%}



%union {

    char* str;  // Use char* for expressions

}



%token <str> NUMBER

%token PLUS MINUS TIMES DIVIDE LPAREN RPAREN



%left PLUS MINUS

%left TIMES DIVIDE

%nonassoc UMINUS



%type <str> expr



%%



input:

    /* empty */

    | input line

;



line:

    expr '\n' { printf("Postfix: %s\n", $1); }

;



expr:

    NUMBER { $$ = strdup($1); }  // Copy the number as a string

    | expr PLUS expr { 

        $$ = concat($1, concat($3, " + ")); 

    }

    | expr MINUS expr { 

        $$ = concat($1, concat($3, " - ")); 

    }

    | expr TIMES expr { 

        $$ = concat($1, concat($3, " * ")); 

    }

    | expr DIVIDE expr { 

        $$ = concat($1, concat($3, " / ")); 

    }

    | LPAREN expr RPAREN { 

        $$ = $2;  // Parentheses don't change the expression

    }

    | MINUS expr %prec UMINUS { 

        $$ = concat($2, "NEG ");  // Handle unary minus

    }

;



%%



void yyerror(const char *s) {

    fprintf(stderr, "%s\n", s);

}



// Helper function to concatenate two strings

char* concat(const char *s1, const char *s2) {

    char *result = malloc(strlen(s1) + strlen(s2) + 1);

    strcpy(result, s1);

    strcat(result, s2);

    return result;

}



int main() {

    printf("Enter infix expression:\n");

    yyparse();

    return 0;

}
