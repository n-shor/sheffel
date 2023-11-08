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

int main(int argc, char *argv[]) 
{
    if(argc < 2)
    {
        std::cout << "Please provide a file path as an argument.\n";
        return 1;
    }
    
    yyin = fopen(argv[1], "r");

    if (!yyin)
    {
        std::cout << "Could not open " << argv[1] << " for reading.\n";
        return 1;
    }

    yyparse();

    fclose(yyin);
}

void yyerror(const char *s)
{
  std::cerr << "Error: " << s << "\n";
}

void cleanAST(Node* node)
{
    if (node == nullptr) return;

    cleanAST(node->left);
    cleanAST(node->right);

    delete node;
}

void printAST(Node* node, int depth)
{
    if (node == nullptr) return;

    std::cout << std::string(2 * depth, ' ') << node->value << "\n";

    printAST(node->left, depth + 1);
    printAST(node->right, depth + 1);
}