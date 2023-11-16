#pragma once

#include <string>
#include <vector>
#include <iostream>
#include <sstream>

struct Node
{
    std::string value;
    std::vector<Node*> children;

    static void clean(Node* node);
    static std::string json(Node* node);
};

static Node* root = nullptr;

int evaluate(Node* node);
void yyerror(const char *s);

