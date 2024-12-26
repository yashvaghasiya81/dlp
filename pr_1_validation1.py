def isValid(s):
    length = len(s) - 1  
    if length < 2:
        return False
    elif length == 2:
        if s[0] == 'b' and s[1] == 'b':
            return True
        else:
            return False
    else:
        for i in range(length - 2):
            if s[i] != 'a':
                return False
        for i in range(length - 2, length):
            if s[i] != 'b':
                return False
    return True


def main():
    s = input("Enter string: ")
    if isValid(s):
        print("String is valid")
    else:
        print("String is invalid")


if __name__ == "__main__":
    main()
