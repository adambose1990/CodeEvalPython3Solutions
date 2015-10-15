import sys

test_cases = open('C:/Users/Arindam/workspaceCodeEval/CodeEvalEasy/files/test_JollyJumpers.txt', 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...
    nums = test.split()
    intNum = map(int, nums)
    listNums = list(intNum)[1:]
    
    results = [abs(listNums[i] - listNums[i - 1]) for i in range(1, len(listNums))]
    results = sorted(results)
    resultsDup = list(range(1, len(results) + 1))
    if results == resultsDup :
        print('Jolly')
    else:
        print('Not jolly')
                
test_cases.close()