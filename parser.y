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
    expr '\n'  { 
        std::cout << "AST: " << std::endl;
        std::cout << Node::json($1) << std::endl;
        Node::clean($1);
    }
;

expr:
    NUMBER          { $$ = new Node{std::to_string($1)}; }
|   expr '+' expr   { $$ = new Node{"+", {$1, $3}}; }
|   expr '-' expr   { $$ = new Node{"-", {$1, $3}}; }
|   expr '*' expr   { $$ = new Node{"*", {$1, $3}}; }
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

    getchar();
}

void yyerror(const char *s)
{
  std::cerr << "Error: " << s << "\n";
}

void Node::clean(Node* node)
{
    for (Node* child : node->children)
        clean(child);

    delete node;
}

std::string Node::json(Node* node)
{
    if (node->children.size() == 0) return node->value;

    std::ostringstream oss;

    oss << "[" << node->value;

    for (Node* child : node->children)
        oss << ", " << json(child);

    oss << "]";

    return std::move(oss).str();
}