%{

#include <stdio.h>

#include <stdlib.h>



void yyerror(const char *s);

int yylex();

%}



%union {

    int num;  // Use int for storing numbers

}



%token <num> NUMBER

%token PLUS MINUS TIMES DIVIDE



%type <num> expr  // Declare that expr will store integer values



%%



input:

    /* empty */

    | input line

;



line:

    expr '\n' { printf("Result: %d\n", $1); }

;



expr:

    NUMBER { $$ = $1; }  // Push number onto the stack

    | expr expr PLUS { $$ = $1 + $2; }  // Pop two numbers, perform addition, and push result

    | expr expr MINUS { $$ = $1 - $2; }  // Pop two numbers, perform subtraction, and push result

    | expr expr TIMES { $$ = $1 * $2; }  // Pop two numbers, perform multiplication, and push result

    | expr expr DIVIDE { 

        if ($2 == 0) {

            yyerror("Division by zero");

            YYABORT;

        }

        $$ = $1 / $2;  // Pop two numbers, perform division, and push result

    }

;



%%



void yyerror(const char *s) {

    fprintf(stderr, "%s\n", s);

}



int main() {

    printf("Enter postfix expression:\n");

    yyparse();

    return 0;

}
