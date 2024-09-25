%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SYMBOL_TABLE_SIZE 100

typedef struct {
    char *name;
    char *type;
} symbol_t;

symbol_t symbol_table[SYMBOL_TABLE_SIZE];
int symbol_count = 0;

void insert_symbol(char *name, char *type);
int lookup_symbol(char *name);
void print_symbol_table();

extern int yylex();
void yyerror(const char *s);
%}

/* Define a union to hold different types of values */
%union {
    char *str;  /* For IDENTIFIER */
}

/* Define tokens with the corresponding type from %union */
%token <str> IDENTIFIER
%token INT FLOAT CHAR DOUBLE
%token SEMICOLON

%type <str> type identifier

%%

program:
    declarations /* Main entry point */
    ;

declarations:
    declarations declaration
    | declaration
    ;

declaration:
    type identifier SEMICOLON { 
        if (lookup_symbol($2) == -1) {
            insert_symbol($2, $1); 
        } else {
            printf("Error: Variable '%s' is already declared.\n", $2);
        }
    }
    ;

type:
    INT    { $$ = "int"; }
    | FLOAT  { $$ = "float"; }
    | CHAR   { $$ = "char"; }
    | DOUBLE { $$ = "double"; }
    ;

identifier:
    IDENTIFIER { $$ = $1; }
    ;

%%

void insert_symbol(char *name, char *type) {
    if (symbol_count < SYMBOL_TABLE_SIZE) {
        symbol_table[symbol_count].name = strdup(name);
        symbol_table[symbol_count].type = strdup(type);
        symbol_count++;
    } else {
        printf("Error: Symbol table overflow.\n");
    }
}

int lookup_symbol(char *name) {
    for (int i = 0; i < symbol_count; i++) {
        if (strcmp(symbol_table[i].name, name) == 0) {
            return i;  // Found
        }
    }
    return -1;  // Not found
}

void print_symbol_table() {
    printf("\nSymbol Table:\n");
    printf("Name\tType\n");
    printf("----------------\n");
    for (int i = 0; i < symbol_count; i++) {
        printf("%s\t%s\n", symbol_table[i].name, symbol_table[i].type);
    }
}

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main() {
    printf("Enter variable declarations (end input with Ctrl+D):\n");
    yyparse();
    print_symbol_table();
    return 0;
}

