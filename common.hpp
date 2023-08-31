#pragma once

#include <string>
#include <iostream>

struct Node {
    std::string value;
    Node* left = nullptr;
    Node* right = nullptr;
};

static Node* root = nullptr;

int evaluate(Node* node);
void printAST(Node* node, int depth = 0);
void yyerror(const char *s);

