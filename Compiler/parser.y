%{
#include "common.hpp"
extern int yylex();
extern FILE *yyin;
%}

%union
{
    int val;
    Node* node;
}

%token <val> NUMBER
%token ';'
%left '+' '-'
%left '*'
%type <node> expr
%type <node> command

%%

program:
    /* empty */
|   program command
;

command:
    expr ';'  { 
        std::cout << "AST: " << std::endl; 
        printAST($1);
        cleanAST($1);
    }
;

expr:
    NUMBER          { $$ = new Node{std::to_string($1)}; }
|   expr '+' expr   { $$ = new Node{"+", $1, $3}; }
|   expr '-' expr   { $$ = new Node{"-", $1, $3}; }
|   expr '*' expr   { $$ = new Node{"*", $1, $3}; }
|   '(' expr ')'    { $$ = $2; }
;

%%

int parser_main(int argc, const char *argv[]) 
{
    if(argc < 2) {
        std::cout << "Please provide a file path as an argument.\n";
        return 1;
    }
    
    yyin = fopen(argv[1], "r");
    if (!yyin) {
        std::cout << "Could not open " << argv[1] << " for reading.\n";
        return 1;
    }

    yyparse();

    fclose(yyin);
    return 0;
}

void yyerror(const char *s)
{
  std::cerr << "Error: " << s << std::endl;
}

void cleanAST(Node* node)
{
    if (node == nullptr) return;

    if (node->left == nullptr && node->right == nullptr) delete node;

    cleanAST(node->left);
    cleanAST(node->right);
}

void printAST(Node* node, int depth)
{
    if (node == nullptr) return;

    for (int i = 0; i < depth; ++i)
    {
        std::cout << "  ";
    }

    std::cout << node->value << "\n";
    printAST(node->left, depth + 1);
    printAST(node->right, depth + 1);
}