%{
#include "common.hpp"
extern int yylex();
%}

%union
{
    int val;
    Node* node;
}

%token <val> NUMBER
%token '\n'
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
        std::cout << "Result: " << evaluate($1) << std::endl; 
        std::cout << "AST: " << std::endl; 
        printAST($1);
        delete $1;
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

int main() 
{
    std::cout << "Enter expressions followed by a newline or type 'exit' to quit.\n";
    yyparse();
    return 0;
}

void yyerror(const char *s)
{
  std::cerr << "Error: " << s << std::endl;
}

int evaluate(Node* node)
{
    if (node->left == nullptr && node->right == nullptr)
    {
        return std::stoi(node->value);
    }
    int leftValue = evaluate(node->left);
    int rightValue = evaluate(node->right);
    if (node->value == "+") return leftValue + rightValue;
    if (node->value == "-") return leftValue - rightValue;
    if (node->value == "*") return leftValue * rightValue;
    return 0;
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