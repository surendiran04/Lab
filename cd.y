%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    char *name;
    struct Node **children;
    int children_count;
} Node;

Node *create_node(char *name);
void add_child(Node *parent, Node *child);
void print_tree(Node *node, int level);
void free_tree(Node *node);

#define YYSTYPE Node*
%}

%union {
    char *str;
    Node *node;
}

%token TAG_OPEN TAG_CLOSE TAG_END TAG_SELF_CLOSE COMMENT_START COMMENT_END ATTR_VALUE EQUALS
%token IDENTIFIER CLASS_NAME ID_NAME CSS_PROPERTY COLON SEMICOLON CSS_COMMENT_START CSS_COMMENT_END
%token MEDIA IMPORT AT_RULE PSEUDO_CLASS TEXT NUMBER

%%

html_document
    : elements { print_tree($1, 0); free_tree($1); }
    ;

element
    : TAG_OPEN IDENTIFIER attributes TAG_SELF_CLOSE { $$ = create_node("self_closing"); add_child($$, create_node($2)); add_child($$, $3); }
    | TAG_OPEN IDENTIFIER attributes TAG_END elements TAG_CLOSE IDENTIFIER { $$ = create_node($2); add_child($$, $3); add_child($$, $5); }
    | TAG_OPEN IDENTIFIER attributes TAG_END TAG_CLOSE { $$ = create_node($2); add_child($$, $3); }
    ;

elements
    : element { $$ = create_node("elements"); add_child($$, $1); }
    | elements element { add_child($1, $2); $$ = $1; }
    | TEXT { $$ = create_node("text"); add_child($$, create_node($1)); }
    | COMMENT_START TEXT COMMENT_END { $$ = create_node("comment"); add_child($$, create_node($2)); }
    ;

attributes
    : IDENTIFIER EQUALS ATTR_VALUE { $$ = create_node("attribute"); add_child($$, create_node($1)); add_child($$, create_node($3)); }
    | attributes IDENTIFIER EQUALS ATTR_VALUE { add_child($1, create_node($2)); add_child($1, create_node($4)); $$ = $1; }
    | /* empty */ { $$ = create_node("attributes"); }
    ;

css
    : css_rules { print_tree($1, 0); free_tree($1); }
    ;

css_rules
    : css_rule { $$ = create_node("css_rules"); add_child($$, $1); }
    | css_rules css_rule { add_child($1, $2); $$ = $1; }
    ;

css_rule
    : CSS_SELECTOR BRACE_OPEN declarations BRACE_CLOSE { $$ = create_node("css_rule"); add_child($$, create_node($1)); add_child($$, $3); }
    | MEDIA IDENTIFIER BRACE_OPEN css_rules BRACE_CLOSE { $$ = create_node("media_rule"); add_child($$, create_node($2)); add_child($$, $4); }
    | IMPORT IDENTIFIER SEMICOLON { $$ = create_node("import_rule"); add_child($$, create_node($2)); }
    | AT_RULE BRACE_OPEN declarations BRACE_CLOSE { $$ = create_node("at_rule"); add_child($$, create_node($1)); add_child($$, $3); }
    ;

declarations
    : declaration { $$ = create_node("declarations"); add_child($$, $1); }
    | declarations declaration { add_child($1, $2); $$ = $1; }
    | CSS_COMMENT_START TEXT CSS_COMMENT_END { $$ = create_node("css_comment"); add_child($$, create_node($2)); }
    ;

declaration
    : CSS_PROPERTY COLON CSS_VALUE SEMICOLON { $$ = create_node("declaration"); add_child($$, create_node($1)); add_child($$, create_node($3)); }
    | CSS_PROPERTY COLON NUMBER SEMICOLON { $$ = create_node("declaration"); add_child($$, create_node($1)); add_child($$, create_node($3)); }
    ;

%%

Node* create_node(char *name) {
    Node *node = (Node *)malloc(sizeof(Node));
    node->name = strdup(name);
    node->children = NULL;
    node->children_count = 0;
    return node;
}

void add_child(Node *parent, Node *child) {
    parent->children = realloc(parent->children, sizeof(Node*) * (parent->children_count + 1));
    parent->children[parent->children_count++] = child;
}

void print_tree(Node *node, int level) {
    for (int i = 0; i < level; i++) printf("  ");
    printf("%s\n", node->name);
    for (int i = 0; i < node->children_count; i++) {
        print_tree(node->children[i], level + 1);
    }
}

void free_tree(Node *node) {
    free(node->name);
    for (int i = 0; i < node->children_count; i++) {
        free_tree(node->children[i]);
    }
    free(node->children);
    free(node);
}

int main() {
    yyparse();
    return 0;
}

int yyerror(const char *s) {
    fprintf(stderr, "Parse error: %s\n", s);
    return 1;
}
