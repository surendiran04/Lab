%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void yyerror(const char *s);
int yylex(void);

typedef struct node {
    char *token;
    struct node *left;
    struct node *middle1;
    struct node *middle2;
    struct node *right;
} Node;

Node* create_node(char* token, Node* left, Node* middle1, Node* middle2, Node* right);
void print_tree(Node* root, int depth, int is_left);

%}

%union {
    char* str;         // For tokens like ID and NUM
    struct node* node; // For the parse tree nodes
}

// Declare token types (with type information for semantic values)
%token <str> ID NUM
%token <str> WHILE LE GE EQ NE OR AND FOR

// Declare non-terminal types
%type <node> S ST1 ST E E2

%right '='
%left AND OR
%left '<' '>' LE GE EQ NE
%left '+' '-'
%left '*' '/'
%right UMINUS
%left '!'

%%

// Start rule
prog:
    S prog
    |
    ;

// For loop statement
S:
    ST1 { print_tree($1, 0, 1); }
    ;

ST1:
    FOR '(' E ';' E2 ';' E ')' '{' ST '}' 
    {
        $$ = create_node("for",
            create_node("stmt", create_node("(",$3,NULL,NULL,NULL), create_node(";", NULL, NULL, NULL, NULL), 
            $5, create_node(";", NULL, NULL, NULL, NULL)),
            $7,create_node("{", $10,NULL,NULL,NULL),create_node("}",NULL,NULL,NULL,NULL));
    }
    ;

// Statements within the loop
ST:
    E ';' ST
    {
        Node* semicolon = create_node(";", NULL, NULL, NULL, NULL);
        $$ = create_node("stmt", $1, semicolon, $3, NULL);
    }
    |
    {
	$$ = create_node("empty",NULL,NULL,NULL,NULL);
    } 
    ;

// Expression rules
E:
    ID '=' E
    {
        Node* assign_node = create_node("=", NULL, NULL, NULL, NULL);
        $$ = create_node("assign", create_node($1, NULL, NULL, NULL, NULL), assign_node, $3, NULL);
    }
    | E '+' E
    {
        $$ = create_node("+", $1, NULL, $3, NULL);
    }
    | E '-' E
    {
        $$ = create_node("-", $1, NULL, $3, NULL);
    }
    | E '*' E
    {
        $$ = create_node("*", $1, NULL, $3, NULL);
    }
    | E '/' E
    {
        $$ = create_node("/", $1, NULL, $3, NULL);
    }
    | E '<' E
    {
        $$ = create_node("<", $1, NULL, $3, NULL);
    }
    | E '>' E
    {
        $$ = create_node(">", $1, NULL, $3, NULL);
    }
    | E LE E
    {
        $$ = create_node("<=", $1, NULL, $3, NULL);
    }
    | E GE E
    {
        $$ = create_node(">=", $1, NULL, $3, NULL);
    }
    | E EQ E
    {
        $$ = create_node("==", $1, NULL, $3, NULL);
    }
    | E NE E
    {
        $$ = create_node("!=", $1, NULL, $3, NULL);
    }
    | E OR E
    {
        $$ = create_node("||", $1, NULL, $3, NULL);
    }
    | E AND E
    {
        $$ = create_node("&&", $1, NULL, $3, NULL);
    }
    | ID
    {
        $$ = create_node($1, NULL, NULL, NULL, NULL);
    }
    | NUM
    {
        $$ = create_node($1, NULL, NULL, NULL, NULL);
    }
    ;

E2:
    E '<' E
    {
        $$ = create_node("<", $1, NULL, $3, NULL);
    }
    | E '>' E
    {
        $$ = create_node(">", $1, NULL, $3, NULL);
    }
    | E LE E
    {
        $$ = create_node("<=", $1, NULL, $3, NULL);
    }
    | E GE E
    {
        $$ = create_node(">=", $1, NULL, $3, NULL);
    }
    | E EQ E
    {
        $$ = create_node("==", $1, NULL, $3, NULL);
    }
    | E NE E
    {
        $$ = create_node("!=", $1, NULL, $3, NULL);
    }
    | E OR E
    {
        $$ = create_node("||", $1, NULL, $3, NULL);
    }
    | E AND E
    {
        $$ = create_node("&&", $1, NULL, $3, NULL);
    }
    | ID
    {
        $$ = create_node($1, NULL, NULL, NULL, NULL);
    }
    | NUM
    {
        $$ = create_node($1, NULL, NULL, NULL, NULL);
    }
    ;

%%

// Node creation function
Node* create_node(char* token, Node* left, Node* middle1, Node* middle2, Node* right) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->token = strdup(token);
    new_node->left = left;
    new_node->middle1 = middle1;
    new_node->middle2 = middle2;
    new_node->right = right;
    return new_node;
}

// Tree printing function
void print_tree(Node* root, int depth, int is_left) {
    if (root == NULL) return;

    for (int i = 0; i < depth - 1; i++) {
        printf("    ");
    }

    if (depth > 0) {
        if (is_left) {
            printf("  /---- ");
        } else {
            printf("  \\---- ");
        }
    }

    printf("%s\n", root->token);

    if (root->left) print_tree(root->left, depth + 1, 1);
    if (root->middle1) print_tree(root->middle1, depth + 1, 0);
    if (root->middle2) print_tree(root->middle2, depth + 1, 0);
    if (root->right) print_tree(root->right, depth + 1, 0);
}

// Error handler
void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

// Main function
int main() {
    printf("Enter the 'for' loop to parse:\n");
    yyparse();
    return 0;
}

