%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int temp_count = 0;
int label_count = 0;

void generate_tac(char *result, char *arg1, char *op, char *arg2) {
    printf("%s = %s %s %s\n", result, arg1, op, arg2);
}

void generate_array_tac(char *arr, char *index, char *result) {
    printf("%s = %s[%s]\n", result, arr, index);
}

void generate_assignment_tac(char *var, char *value) {
    printf("%s = %s\n", var, value);
}

void generate_label(int label) {
    printf("L%d:\n", label);
}

void generate_goto(int label) {
    printf("goto L%d\n", label);
}

void generate_if_goto(char *cond, int label) {
    printf("if %s goto L%d\n", cond, label);
}

%}

%token ID NUM
%left '+' '-'
%left '*' '/'
%token FOR WHILE IF ELSE
%token LT GT LE GE EQ NE
%token LBRACKET RBRACKET LPAR RPAR LBRACE RBRACE ASSIGN

%%

stmt_list
    : stmt stmt_list
    | /* Empty */
    ;

stmt
    : expr ';' { printf("Result: %s\n", $1); }
    | assignment ';'
    | for_loop
    | while_loop
    | if_else
    ;

assignment
    : ID ASSIGN expr {
          generate_assignment_tac($1, $3);
      }
    | ID LBRACKET expr RBRACKET ASSIGN expr {
          char temp[5];
          sprintf(temp, "t%d", temp_count++);
          generate_array_tac($1, $3, temp);
          generate_assignment_tac(temp, $6);
      }
    ;

for_loop
    : FOR LPAR assignment ';' condition ';' assignment RPAR stmt {
          int start_label = label_count++;
          int end_label = label_count++;
          generate_label(start_label);
          generate_if_goto($3, end_label);
          printf("Loop Body:\n");
          $$ = $8;
          $$ = $7;
          generate_goto(start_label);
          generate_label(end_label);
      }
    ;

while_loop
    : WHILE LPAR condition RPAR stmt {
          int start_label = label_count++;
          int end_label = label_count++;
          generate_label(start_label);
          generate_if_goto($3, end_label);
          $$ = $5;
          generate_goto(start_label);
          generate_label(end_label);
      }
    ;

if_else
    : IF LPAR condition RPAR stmt ELSE stmt {
          int else_label = label_count++;
          int end_label = label_count++;
          generate_if_goto($3, else_label);
          $$ = $5;
          generate_goto(end_label);
          generate_label(else_label);
          $$ = $7;
          generate_label(end_label);
      }
    ;

condition
    : expr LT expr { 
          char temp[5]; 
          sprintf(temp, "t%d", temp_count++); 
          generate_tac(temp, $1, "<", $3); 
          $$ = strdup(temp); 
      }
    | expr GT expr {
          char temp[5];
          sprintf(temp, "t%d", temp_count++);
          generate_tac(temp, $1, ">", $3);
          $$ = strdup(temp);
      }
    | expr LE expr {
          char temp[5];
          sprintf(temp, "t%d", temp_count++);
          generate_tac(temp, $1, "<=", $3);
          $$ = strdup(temp);
      }
    | expr GE expr {
          char temp[5];
          sprintf(temp, "t%d", temp_count++);
          generate_tac(temp, $1, ">=", $3);
          $$ = strdup(temp);
      }
    | expr EQ expr {
          char temp[5];
          sprintf(temp, "t%d", temp_count++);
          generate_tac(temp, $1, "==", $3);
          $$ = strdup(temp);
      }
    | expr NE expr {
          char temp[5];
          sprintf(temp, "t%d", temp_count++);
          generate_tac(temp, $1, "!=", $3);
          $$ = strdup(temp);
      }
    ;

expr
    : expr '+' expr {
          char temp[5];
          sprintf(temp, "t%d", temp_count++);
          generate_tac(temp, $1, "+", $3);
          $$ = strdup(temp);
      }
    | expr '-' expr {
          char temp[5];
          sprintf(temp, "t%d", temp_count++);
          generate_tac(temp, $1, "-", $3);
          $$ = strdup(temp);
      }
    | expr '*' expr {
          char temp[5];
          sprintf(temp, "t%d", temp_count++);
          generate_tac(temp, $1, "*", $3);
          $$ = strdup(temp);
      }
    | expr '/' expr {
          char temp[5];
          sprintf(temp, "t%d", temp_count++);
          generate_tac(temp, $1, "/", $3);
          $$ = strdup(temp);
      }
    | ID { $$ = strdup(yytext); }
    | NUM { $$ = strdup(yytext); }
    | ID LBRACKET expr RBRACKET {
          char temp[5];
          sprintf(temp, "t%d", temp_count++);
          generate_array_tac($1, $3, temp);
          $$ = strdup(temp);
      }
    ;

%%
int main() {
    printf("Enter the code:\n");
    yyparse();
    return 0;
}

int yyerror(char *s) {
    printf("Error: %s\n", s);
    return 0;
}
