#ifndef COMMON_H
#define COMMON_H

#include <string>
#include <iostream>

struct Node {
    std::string value;
    Node* left = nullptr;
    Node* right = nullptr;
};

extern Node* root;

int evaluate(Node* node);
void printAST(Node* node, int depth = 0);
void yyerror(const char *s);

#endif // COMMON_H
