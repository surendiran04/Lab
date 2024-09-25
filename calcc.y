%{                                                                                                                                                       
#include <stdio.h>                                                                                                                                       
#include <stdlib.h>                                                                                                                                      
%}                                                                                                                                                       
/* Tokens */                                                                                                                                             
%token NUMBER                                                                                                                                            
%left '+' '-'                                                                                                                                            
%left '*' '/'                                                                                                                                            
%%                                                                                                                                                       

/* Grammar rules and actions */                                                                                                                          
calculation:                                                                                                                                             
/* empty */                                                                                                                                              
| calculation expr '\n' { printf("Result = %d\n", $2); }                                                                                                 
;                                                                                                                                                        
expr:                                                                                                                                                    
expr '+' expr { $$ = $1 + $3; }                                                                                                                          
| expr '-' expr { $$ = $1 - $3; }                                                                                                                        
| expr '*' expr { $$ = $1 * $3; }                                                                                                                        
| expr '/' expr {                                                                                                                                        
if ($3 == 0) {                                                                                                                                           
yyerror("Division by zero");                                                                                                                             
YYABORT;                                                                                                                                                 

} else {                                                                                                                                                 

$$ = $1 / $3;                                                                                                                                            

}                                                                                                                                                        

}                                                                                                                                                        

| '(' expr ')' { $$ = $2; }                                                                                                                              

| NUMBER       { $$ = $1; }                                                                                                                              

;                                                                                                                                                        

%%                                                                                                                                                       

/* Auxiliary functions */                                                                                                                                

int main() {                                                                                                                                             

printf("Enter expressions followed by a newline. Type 'Ctrl+D' to exit.\n");                                                                             

yyparse();                                                                                                                                               

return 0;                                                                                                                                                

}                                                                                                                                                        

void yyerror(char *s) {                                                                                                                                  

fprintf(stderr, "Error: %s\n", s);                                                                                                                       

}
