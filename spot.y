%{
#include <stdio.h>
#include <stdlib.h>
void yyerror(const char *s);
int yylex(void);
extern FILE *yyin;
%}
%token SWITCH CASE DEFAULT BREAK COLON SEMICOLON NUM IDENTIFIER LBRACE RBRACE                                                  
%%                                                                                                                             
program:switch_statement                                                                                                        
       ;
switch_statement:SWITCH '(' IDENTIFIER ')' LBRACE cases RBRACE                                                              
                ;
cases:case_list                                                                                                             
     | case_list default_case                                                                                                   
     | default_case                                                                                                             
     ;
case_list:case_list case_statement                                                                                          
         | case_statement                                                                                                           
         ;
case_statement:CASE NUM COLON statements                                                                                    
              ;
default_case:DEFAULT COLON statements                                                                                       
            ;
statements:statements statement                                                                                             
          | statement                                                                                                                
          ;
statement:IDENTIFIER SEMICOLON                                                                                              
         | BREAK SEMICOLON                                                                                                          
         ;                                                                                                                          
%%                                                                                                                             
void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}
int main(int argc, char **argv) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <input_file>\n", argv[0]);
        return 1;
    }
    FILE *input_file = fopen(argv[1], "r");
    if (!input_file) {
        perror("fopen");
        return 1;
    }
    yyin = input_file;
    if (yyparse() == 0) {
        printf("Switch-case statement is valid.\n");
    } else {
        printf("Switch-case statement is invalid.\n");
    }
    fclose(input_file);
    return 0;
} 
