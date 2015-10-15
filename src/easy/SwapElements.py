import sys

test_cases = open('C:/Users/Arindam/workspaceCodeEval/CodeEvalEasy/files/test_SwapElements.txt', 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...
    parts = test.split(':');
    arrStr = parts[0].split();
    swapDistances = parts[1].split(',');
    for num in swapDistances :
        distance = num.split('-');
        start = int(distance[0]);
        end = int(distance[1]);
        temp = arrStr[start];
        arrStr[start] = arrStr[end];
        arrStr[end] = temp;
    builder = '';
    for num in arrStr :
        builder = builder + num + ' '
    builder = builder[:len(builder)-1]
    print(builder)

test_cases.close()