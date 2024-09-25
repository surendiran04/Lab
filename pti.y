%{

#include <stdio.h>

#include <stdlib.h>

#include <string.h>



void yyerror(const char *s);

int yylex();

char* concat(const char *s1, const char *s2);

char* wrap(const char *s1, const char *s2, const char *s3);

%}



%union {

    char* str;  // For storing expressions as strings

}



%token <str> NUMBER

%token PLUS MINUS TIMES DIVIDE



%type <str> expr



%%



input:

    /* empty */

    | input line

;



line:

    expr '\n' { printf("Infix: %s\n", $1); }

;



expr:

    NUMBER { $$ = strdup($1); }  // Push the operand to the stack (store the number)

    | expr expr PLUS { 

        $$ = wrap($1, " + ", $2);  // Pop two operands and create infix: (operand1 + operand2)

    }

    | expr expr MINUS { 

        $$ = wrap($1, " - ", $2);  // Pop two operands and create infix: (operand1 - operand2)

    }

    | expr expr TIMES { 

        $$ = wrap($1, " * ", $2);  // Pop two operands and create infix: (operand1 * operand2)

    }

    | expr expr DIVIDE { 

        $$ = wrap($1, " / ", $2);  // Pop two operands and create infix: (operand1 / operand2)

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



// Helper function to wrap an expression in parentheses: (s1 operator s2)

char* wrap(const char *s1, const char *operator, const char *s2) {

    char *result = malloc(strlen(s1) + strlen(operator) + strlen(s2) + 3);  // Extra space for parentheses and null character

    sprintf(result, "(%s%s%s)", s1, operator, s2);

    return result;

}



int main() {

    printf("Enter postfix expression:\n");

    yyparse();

    return 0;

}
