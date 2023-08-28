%{
#include <iostream>
#include <string>

// AST Node Structure
struct Node {
    std::string value;  // Node value
    Node* left = nullptr;  // Left child
    Node* right = nullptr; // Right child
};

// Function to evaluate AST
int evaluate(Node* node) {
    if (node->left == nullptr && node->right == nullptr) {
        return std::stoi(node->value);
    }
    int leftValue = evaluate(node->left);
    int rightValue = evaluate(node->right);
    if (node->value == "+") return leftValue + rightValue;
    if (node->value == "-") return leftValue - rightValue;
    if (node->value == "*") return leftValue * rightValue;
    return 0; // Should never reach here
}

// Function to print AST
void printAST(Node* node, int depth = 0) {
    if (node == nullptr) return;
    
    for (int i = 0; i < depth; ++i) {
        std::cout << "  ";
    }
    std::cout << node->value << "\n";
    printAST(node->left, depth + 1);
    printAST(node->right, depth + 1);
}
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
    NUMBER          { $$ = new Node{std::to_string($1)}; }  // Leaf node
|   expr '+' expr   { $$ = new Node{"+", $1, $3}; }         // Addition
|   expr '-' expr   { $$ = new Node{"-", $1, $3}; }         // Subtraction
|   expr '*' expr   { $$ = new Node{"*", $1, $3}; }         // Multiplication
|   '(' expr ')'    { $$ = $2; }                            // Parentheses
;

%%

int main() {
    Node* root = nullptr;

    // Main loop to keep parsing expressions until 'exit' is entered
    while (true) {
        std::cout << "Enter an expression or 'exit' to quit: ";
        if (yyparse() == 0) {
            std::cout << "Result: " << evaluate(root) << "\n";
            std::cout << "AST:\n";
            printAST(root);
        }
        std::string exitCheck;
        std::getline(std::cin, exitCheck);
        if (exitCheck == "exit") {
            break;
        }
    }

    return 0;
}

void yyerror(const char *msg) {
    std::cerr << "Error: " << msg << std::endl;
}