%{                                                                                                                                          
#include <stdio.h>                                                                                                                          
#include <stdlib.h>                                                                                                                         
int yylex(void);                                                                                                                            
void yyerror(const char *s);                                                                                                                
%}                                                                                                                                          
%token ID NUM LE GE EQ NE OR AND FOR                                                                                                        
%right '='                                                                                                                                  
%left AND OR                                                                                                                                
%left '<' '>' LE GE EQ NE                                                                                                                   
%left '+''-'                                                                                                                                
%left '*''/'                                                                                                                                
%right UMINUS                                                                                                                               
%left '!'                                                                                                                                   
%%                                                                                                                                          
prog: S prog                                                                                                                                
    |                                                                                                                                       
    ;                                                                                                                                       
S: ST1 {printf("Input Accepted!!!\n");}                                                                                                     
 ;                                                                                                                                          
ST1: FOR '(' E ';' E2 ';' E ')' '{' ST '}'                                                                                                  
ST: E';' ST                                                                                                                                 
  |                                                                                                                                         
  ;                                                                                                                                         
E: ID'='E                                                                                                                                   
 | E'+'E                                                                                                                                    
 | E'-'E                                                                                                                                    
 | E'*'E                                                                                                                                    
 | E'/'E                                                                                                                                    
 | E'<'E                                                                                                                                    
 | E'>'E                                                                                                                                    
 | E LE E                                                                                                                                   
 | E GE E                                                                                                                                   
 | E EQ E                                                                                                                                   
 | E NE E                                                                                                                                   
 | E OR E                                                                                                                                   
 | E AND E                                                                                                                                  
 | ID                                                                                                                                       
 | NUM                                                                                                                                      
 | E '+''=' E                                                                                                                               
 | E '-''=' E                                                                                                                               
 | E '+''+'                                                                                                                                 
 | E '-''-'                                                                                                                                 
 ;                                                                                                                                          
E2: E'<'E                                                                                                                                   
  | E'>'E                                                                                                                                   
  | E LE E                                                                                                                                  
  | E GE E                                                                                                                                  
  | E EQ E                                                                                                                                  
  | E NE E                                                                                                                                  
  | E OR E                                                                                                                                  
  | E AND E                                                                                                                                 
  | ID                                                                                                                                      
  | NUM                                                                                                                                     
  ;                                                                                                                                         
%%                                                                                                                                          
void yyerror(const char *s){                                                                                                                
        printf("%s\n",s);                                                                                                                   
}                                                                                                                                           
int main(){                                                                                                                                 
        yyparse();                                                                                                                          
}
