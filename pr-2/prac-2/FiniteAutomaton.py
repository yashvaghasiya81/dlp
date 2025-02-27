
def isValid(noOfSymbol, inputSymbols, noOfState, initialState, acceptingStates, inputString):
    for char in inputString:
        if char not in inputSymbols:
            return False
    
    transitionTable = {}
    for i in range(1, noOfState + 1):
        transitionTable[i] = {}
        for symbol in inputSymbols:
            tempState = int(input(f"Enter next state if current state is {i} and input symbol is {symbol}: "))
            transitionTable[i][symbol] = tempState
    
    currentState = initialState
    for symbol in inputString:
        if currentState in transitionTable and symbol in transitionTable[currentState]:
            currentState = transitionTable[currentState][symbol]
        else:
            return False
    
    if currentState in acceptingStates:
        return True
    else:
        return False


def main():
    noOfSymbol = int(input("Enter number of input symbols: "))
    inputSymbols = input("Enter input symbols: ")
    noOfState = int(input("Enter number of states: "))
    initialState = int(input("Enter initial state: "))
    noOfAcceptingStates = int(input("Enter number of accepting states: "))
    
    acceptingStates = set()
    print("Enter accepting states: ")
    for _ in range(noOfAcceptingStates):
        acceptingStates.add(int(input()))
    
    inputString = input("Enter input string: ")

    is_valid = isValid(noOfSymbol, inputSymbols, noOfState, initialState, acceptingStates, inputString)

    if is_valid:
        print("The input string is valid.")
    else:
        print("The input string is invalid.")


if __name__ == "__main__":
    main()
