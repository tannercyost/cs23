# as04.py
# Evaluates the truth of a given propositional statement in postfix notation. 

from itertools import product

def findProps(tokens):
    props = set()
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
            props.add(token)
    return props

def calculateTruth(propMap, premise):
    operands = list()
    numOfPushes = 0
    st = list()

    for token in premise:
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

def generateTable(sortedPropList, premises, conclusion):
    propMap = dict()

    for row in product((False, True), repeat=len(sortedPropList)):
        premiseTruthList = list()
        truth = list()
        for item in row:
            truth.append(item)
        for proposition, i in zip(sortedPropList, range(len(truth))):
            propMap[proposition] = truth[i]
        for premise in premises:
            premiseTruthList.append(calculateTruth(propMap, premise.strip().split(" ")))
            conclusionTruth = calculateTruth(propMap, conclusion.strip().split(" "))
        if (all(item == True for item in premiseTruthList) and conclusionTruth == False):
            return False
    return True

inputList = list()
propSet = set()
while True:
    try:
        line = input()
    except EOFError:
        break
    inputList.append(line)
if(len(inputList) > 0):
    conclusion = inputList[-1:][0]
    premises = (inputList[:-1])
    for item in premises:
        propSet.update(findProps(item.strip().split(" ")))
    sortedPropList = list(sorted(propSet))
    print(generateTable(sortedPropList, premises, conclusion))
