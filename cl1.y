%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>

void yyerror(const char *s);
extern int yylex();
extern int yyparse();

FILE *outfile;  // Output file to store the x86 assembly
int temp_var_count = 1;  // Counter for temporary variables (t1, t2, etc.)

void emit(const char *fmt, ...);
char* new_temp();  // Function to generate new temporary variables
%}

%union {
    char *str;
}

%token <str> ID NUM
%token ASSIGN ADD MUL SUB LT IF GOTO COLON NEWLINE END

%type <str> program statements statement expression condition

%%

// Program structure
program:
    statements END { emit("Program successfully converted to x86 assembly.\n"); }
    ;

// Statements structure
statements:
    statements statement { /* Multiple statements */ }
    | statement { /* Single statement */ }
    ;

statement:
    ID ASSIGN expression NEWLINE {
        printf("DEBUG: Assignment statement: %s = %s\n", $1, $3);  // Debugging
        emit("mov eax, [%s]\n", $3);
        emit("mov [%s], eax\n", $1);
    }
    | IF condition GOTO ID NEWLINE {
        printf("DEBUG: If statement: if %s goto %s\n", $2, $4);  // Debugging
        emit("cmp eax, [%s]\n", $2);
        emit("jl %s\n", $4);
    }
    | GOTO ID NEWLINE {
        printf("DEBUG: Goto statement: goto %s\n", $2);  // Debugging
        emit("jmp %s\n", $2);
    }
    | ID COLON NEWLINE {
        printf("DEBUG: Label: %s\n", $1);  // Debugging
        emit("%s:\n", $1);
    }
    ;

// Expression rules
expression:
    ID ADD ID {
        char* temp = new_temp();
        printf("DEBUG: Expression: %s + %s => %s\n", $1, $3, temp);  // Debugging
        emit("mov eax, [%s]\n", $1);
        emit("add eax, [%s]\n", $3);
        emit("mov [%s], eax\n", temp);
        $$ = temp;  // Return the new temporary variable
    }
    | ID MUL ID {
        char* temp = new_temp();
        printf("DEBUG: Expression: %s * %s => %s\n", $1, $3, temp);  // Debugging
        emit("mov eax, [%s]\n", $1);
        emit("imul eax, [%s]\n", $3);
        emit("mov [%s], eax\n", temp);
        $$ = temp;  // Return the new temporary variable
    }
    | ID SUB ID {
        char* temp = new_temp();
        printf("DEBUG: Expression: %s - %s => %s\n", $1, $3, temp);  // Debugging
        emit("mov eax, [%s]\n", $1);
        emit("sub eax, [%s]\n", $3);
        emit("mov [%s], eax\n", temp);
        $$ = temp;  // Return the new temporary variable
    }
    | ID {
        printf("DEBUG: Simple expression: %s\n", $1);  // Debugging
        $$ = $1;  // Use the ID directly
    }
    ;

// Condition rules
condition:
    ID LT ID {
        printf("DEBUG: Condition: %s < %s\n", $1, $3);  // Debugging
        emit("mov eax, [%s]\n", $1);
        emit("cmp eax, [%s]\n", $3);
        $$ = strdup("eax");  // Use the result for further conditions
    }
    ;

%%

// Emit function for generating assembly code
void emit(const char *fmt, ...) {
    va_list args;
    va_start(args, fmt);
    vfprintf(outfile, fmt, args);
    va_end(args);
}

// Function to generate new temporary variables (t1, t2, etc.)
char* new_temp() {
    char* temp = (char*)malloc(10);
    sprintf(temp, "t%d", temp_var_count++);
    return temp;
}

// Error handling
void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

// Main function
int main() {
    outfile = fopen("output.asm", "w");
    if (!outfile) {
        perror("fopen");
        exit(1);
    }
    yyparse();
    fclose(outfile);
    return 0;
}
