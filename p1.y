%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int label_count = 0;
int temp_count = 0;

struct backpatch_list {
    int instr;
    struct backpatch_list *next;
};

struct backpatch_list *create_list(int instr);
void backpatch(struct backpatch_list *list, int label);
struct backpatch_list *merge_lists(struct backpatch_list *list1, struct backpatch_list *list2);
void print_tac(const char* op, const char* arg1, const char* arg2, const char* result);

%}

/* Tokens */
%token FOR WHILE IF ELSE
%token ASSIGN
%token LE GE EQ NE LT GT
%token AND OR
%token NUM ID

/* Non-terminals */
%start program

%%

program:
    stmt_list
;

stmt_list:
    stmt stmt_list
    | /* empty */
;

stmt:
    IF LPAR bool_expr RPAR stmt else_part {
        backpatch($3.true_list, $5.label);
        backpatch($3.false_list, $6.label);
    }
    | WHILE LPAR bool_expr RPAR stmt {
        backpatch($3.true_list, $5.label);
        printf("goto L%d\n", $3.begin_label);
    }
    | FOR LPAR assign_stmt SEMICOLON bool_expr SEMICOLON assign_stmt RPAR stmt {
        backpatch($4.true_list, $8.label);
        printf("goto L%d\n", $4.begin_label);
        backpatch($4.false_list, $8.end_label);
    }
    | assign_stmt SEMICOLON
;

assign_stmt:
    ID ASSIGN expr {
        printf("%s = %s\n", $1, $3);
    }
;

bool_expr:
    expr LT expr {
        char temp[10];
        sprintf(temp, "t%d", temp_count++);
        printf("%s = %s < %s\n", temp, $1, $3);
        $$ = create_list(temp_count - 1);
    }
    | expr GT expr {
        char temp[10];
        sprintf(temp, "t%d", temp_count++);
        printf("%s = %s > %s\n", temp, $1, $3);
        $$ = create_list(temp_count - 1);
    }
    | expr LE expr {
        char temp[10];
        sprintf(temp, "t%d", temp_count++);
        printf("%s = %s <= %s\n", temp, $1, $3);
        $$ = create_list(temp_count - 1);
    }
    | expr GE expr {
        char temp[10];
        sprintf(temp, "t%d", temp_count++);
        printf("%s = %s >= %s\n", temp, $1, $3);
        $$ = create_list(temp_count - 1);
    }
    | expr EQ expr {
        char temp[10];
        sprintf(temp, "t%d", temp_count++);
        printf("%s = %s == %s\n", temp, $1, $3);
        $$ = create_list(temp_count - 1);
    }
    | expr NE expr {
        char temp[10];
        sprintf(temp, "t%d", temp_count++);
        printf("%s = %s != %s\n", temp, $1, $3);
        $$ = create_list(temp_count - 1);
    }
    | bool_expr AND bool_expr {
        backpatch($1.true_list, label_count);
        $$ = merge_lists($1.false_list, $2.false_list);
    }
    | bool_expr OR bool_expr {
        backpatch($1.false_list, label_count);
        $$ = merge_lists($1.true_list, $2.true_list);
    }
;

else_part:
    ELSE stmt
    | /* empty */
;

expr:
    NUM { $$ = $1; }
    | ID { $$ = $1; }
;

%%

/* Functions for backpatching */

struct backpatch_list *create_list(int instr) {
    struct backpatch_list *new_list = (struct backpatch_list *)malloc(sizeof(struct backpatch_list));
    new_list->instr = instr;
    new_list->next = NULL;
    return new_list;
}

void backpatch(struct backpatch_list *list, int label) {
    while (list != NULL) {
        printf("Backpatching instruction %d with label L%d\n", list->instr, label);
        list = list->next;
    }
}

struct backpatch_list *merge_lists(struct backpatch_list *list1, struct backpatch_list *list2) {
    if (!list1) return list2;
    struct backpatch_list *temp = list1;
    while (temp->next != NULL)
        temp = temp->next;
    temp->next = list2;
    return list1;
}

void print_tac(const char* op, const char* arg1, const char* arg2, const char* result) {
    printf("%s = %s %s %s\n", result, arg1, op, arg2);
}

int main() {
    return yyparse();
}
