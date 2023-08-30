%{
#include "common.h"
extern int yylex();
%}

%union {
    int val;
    Node* node;
}

%token <val> NUMBER
%left '+' '-'
%left '*'
%type <node> expr

%%

expr:
    NUMBER          { $$ = new Node{std::to_string($1)}; root = $$; }
|   expr '+' expr   { $$ = new Node{"+", $1, $3}; root = $$; }
|   expr '-' expr   { $$ = new Node{"-", $1, $3}; root = $$; }
|   expr '*' expr   { $$ = new Node{"*", $1, $3}; root = $$; }
|   '(' expr ')'    { $$ = $2; root = $$; }
;

%%

int main() {
    while (true) {
        std::cout << "Enter an expression or type 'exit' to quit: ";
        if (yyparse() == 0 && root != nullptr) {
            std::cout << "Result: " << evaluate(root) << std::endl;
            std::cout << "AST: " << std::endl;
            printAST(root);
        }
        std::string line;
        std::getline(std::cin, line);
        if (line == "exit") break;
    }
    return 0;
}

void yyerror(const char *s) {
  std::cerr << "Error: " << s << std::endl;
}

int evaluate(Node* node) {
    if (node->left == nullptr && node->right == nullptr) {
        return std::stoi(node->value);
    }
    int leftValue = evaluate(node->left);
    int rightValue = evaluate(node->right);
    if (node->value == "+") return leftValue + rightValue;
    if (node->value == "-") return leftValue - rightValue;
    if (node->value == "*") return leftValue * rightValue;
    return 0;
}

void printAST(Node* node, int depth) {
    if (node == nullptr) return;
    for (int i = 0; i < depth; ++i) {
        std::cout << "  ";
    }
    std::cout << node->value << "\n";
    printAST(node->left, depth + 1);
    printAST(node->right, depth + 1);
}
