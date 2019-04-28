def getLength(tokens):
    length = 0
    for token in tokens:
        if (token is None):
            print("Empty string detected.")
        elif (token == "="):
            pass
        elif (token == "->"):
            pass
        elif (token == "<="):
            pass
        elif (token == "+"):
            pass
        elif (token == "*"):
            pass
        elif (token == "!"):
            pass
        elif (token == "~"):
            pass
        elif (token == "True"):
            pass
        elif (token == "False"):
            pass
        else:
            length += 1

    return length

def printTruthTable(length, input, inputString):
    from itertools import product
    propMap = dict()
    for row in product((False, True), repeat=length):
        truth = list()
        for item in row:
            truth.append(item)
            print(item, end="")
            print("\t", end="")
        for proposition, i in zip(input, range(len(truth))):
            propMap[proposition] = truth[i]
        print(calculateTruth(propMap, inputString))

def calculateTruth(propMap, input):
    operands = list()
    numOfPushes = 0
    st = list()

    for token in input:
        if (token is None):
            print("Empty string detected.")
        elif (token == "="):
            operands.clear();
            operands.append(st.pop())
            operands.append(st.pop())
            st.append(operands[0] is operands[1])
        elif (token == "->"):
            operands.clear();
            operands.append(st.pop())
            operands.append(st.pop())
            st.append(operands[0] or not operands[1])
        elif (token == "<="):
            operands.clear();
            operands.append(st.pop())
            operands.append(st.pop())
            st.append(operands[0] or not operands[1])
        elif (token == "+"):
            operands.clear();
            operands.append(st.pop())
            operands.append(st.pop())
            st.append(operands[0] or operands[1])
        elif (token == "*"):
            operands.clear();
            operands.append(st.pop())
            operands.append(st.pop())
            st.append(operands[0] and operands[1])
        elif (token == "!"):
            operands.clear();
            operands.append(st.pop())
            st.append(not operands[0])
        elif (token == "~"):
            operands.clear();
            operands.append(st.pop())
            st.append(not operands[0])
        elif (token == "True"):
            operands.clear();
            operands.append(True)
            st.append(True)
        elif (token == "False"):
            operands.clear();
            operands.append(True)
            st.append(True)
        else:
            st.append(propMap.get(token))
            numOfPushes += 1
            pass

    truthValue = st.pop()
    return truthValue;

def printHeader(length, input, inputString):
    sortedList = list()
    for token in input:
        if (token is None):
            print("Empty string detected.")
        elif (token == "="):
            pass
        elif (token == "->"):
            pass
        elif (token == "<="):
            pass
        elif (token == "+"):
            pass
        elif (token == "*"):
            pass
        elif (token == "!"):
            pass
        elif (token == "~"):
            pass
        elif (token == "True"):
            pass
        elif (token == "False"):
            pass
        else:
            sortedList.append(token)
            pass
    sortedList.sort()
    for item in sortedList:
        print(item, end = '')
        print("\t", end = '')
    for element in inputString:
        print(element, end='')
        print(" ", end='')
    print("")
    return sortedList

inputList = list(input().strip().split(" "))
inputSet = set(inputList)
length = getLength(inputSet)
sortedList = printHeader(length, inputSet, inputList)
printTruthTable(length, sortedList, inputList)
