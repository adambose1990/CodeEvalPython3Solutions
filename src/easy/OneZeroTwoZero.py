import sys
test_cases = open('C:/Users/Arindam/workspaceCodeEval/CodeEvalEasy/files/test_OneZeroTwoZero.txt', 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...
    countTotal = 0
    numStrings = test.split()
    initCount = int(numStrings[0])
    initRange = int(numStrings[1])
    for i in range(1, initRange+1):
        countZero = 0
        binInt = bin(i)[2:] 
        if '0' in binInt:
            countZero = binInt.count('0')
        if countZero == initCount:
            countTotal += 1
    print(countTotal)

test_cases.close()