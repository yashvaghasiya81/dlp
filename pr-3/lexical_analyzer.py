keywords = {"auto",     "break",    "case",     "char", 
            "const",    "continue", "default",  "do", 
            "double",   "else",     "enum",     "extern", 
            "float",    "for",      "goto",     "if", 
            "int",      "long",     "register", "return", 
            "short",    "signed",   "sizeof",   "static", 
            "struct",   "switch",   "typedef",  "union", 
            "unsigned", "void",     "volatile", "while"}
special_symbols = {"+", "-", "*", "/", "=", ";", "(", ")", ",", "{", "}"}

def is_keyword(word):
    return word in keywords

def is_special_symbol(char):
    return char in special_symbols

def lexical_analyzer(source):
    i = 0
    length = len(source)
    tokens = []
    counts = {"Keyword": 0, "Identifier": 0, "Number": 0, "Special Symbol": 0, "Unknown Character": 0}
    
    while i < length:
        if source[i].isspace():
            i += 1
            continue

        if source[i].isalpha():
            token = ""
            while i < length and (source[i].isalnum() or source[i] == "_"):
                token += source[i]
                i += 1
            if is_keyword(token):
                tokens.append(("Keyword", token))
                counts["Keyword"] += 1
            else:
                tokens.append(("Identifier", token))
                counts["Identifier"] += 1
        elif source[i].isdigit():
            token = ""
            while i < length and source[i].isdigit():
                token += source[i]
                i += 1
            tokens.append(("Number", token))
            counts["Number"] += 1
        elif is_special_symbol(source[i]):
            tokens.append(("Special Symbol", source[i]))
            counts["Special Symbol"] += 1
            i += 1
        else:
            tokens.append(("Unknown Character", source[i]))
            counts["Unknown Character"] += 1
            i += 1
    
    return tokens, counts

def main():
    filename = input("Enter the name of the file to analyze: ")
    try:
        with open(filename, "r") as file:
            source_code = file.read()
        print(f"Source Code:\n{source_code}\n")
        
        tokens, counts = lexical_analyzer(source_code)
        print("Tokens:")
        for token_type, token_value in tokens:
            print(f"{token_type}: {token_value}")
        
        print("\nToken Counts:")
        for token_type, count in counts.items():
            print(f"{token_type}: {count}")
        
        print(f"\nTotal Tokens: {sum(counts.values())}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
    main()
