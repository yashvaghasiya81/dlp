#include <iostream>
#include <fstream>
#include <string>
#include <cctype>
#include <vector>

using namespace std;

// List of keywords
const vector<string> keywords = {"int", "float", "if", "else", "while", "for", "return"};

// Function to check if a word is a keyword
bool isKeyword(const string &word) {
    for (const auto &keyword : keywords) {
        if (word == keyword) {
            return true;
        }
    }
    return false;
}

// Function to identify if a character is a special symbol
bool isSpecialSymbol(char ch) {
    string specialSymbols = "+-*/=;(),{}";
    return specialSymbols.find(ch) != string::npos;
}

// Lexical analyzer function
void lexicalAnalyzer(const string &source) {
    size_t i = 0;
    string token;

    cout << "Tokens:" << endl;
    while (i < source.length()) {
        if (isspace(source[i])) {
            i++; // Skip whitespace
            continue;
        }

        // Handle identifiers and keywords
        if (isalpha(source[i])) {
            token.clear();
            while (isalnum(source[i]) || source[i] == '_') {
                token += source[i++];
            }
            if (isKeyword(token)) {
                cout << "Keyword: " << token << endl;
            } else {
                cout << "Identifier: " << token << endl;
            }
        }
        // Handle numbers
        else if (isdigit(source[i])) {
            token.clear();
            while (isdigit(source[i])) {
                token += source[i++];
            }
            cout << "Number: " << token << endl;
        }
        // Handle special symbols
        else if (isSpecialSymbol(source[i])) {
            cout << "Special Symbol: " << source[i] << endl;
            i++;
        }
        // Handle unknown characters
        else {
            cout << "Unknown Character: " << source[i] << endl;
            i++;
        }
    }
}

int main() {
    string filename;
    cout << "Enter the name of the file to analyze: ";
    cin >> filename;

    ifstream file(filename);
    if (!file) {
        cerr << "Error: Unable to open file " << filename << endl;
        return 1;
    }

    // Read the entire file content
    string sourceCode((istreambuf_iterator<char>(file)), istreambuf_iterator<char>());
    file.close();

    cout << "Source Code:\n" << sourceCode << "\n" << endl;

    // Run lexical analysis
    lexicalAnalyzer(sourceCode);

    return 0;
}
