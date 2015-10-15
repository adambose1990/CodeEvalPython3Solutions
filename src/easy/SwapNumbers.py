import sys

test_cases = open('C:/Users/Arindam/workspaceCodeEval/CodeEvalEasy/files/test_SwapNumbers.txt', 'r')
for test in test_cases:
    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...
    words = test.split();
    changed = ""
    for word in words:
        if word[0] != word[len(word)-1] :
            tempWord = word[len(word)-1] + word[1:len(word)-1] + word[0]
            word = tempWord
        changed = changed + word + " "
    changed = changed[:len(changed)-1]
    print(changed)

test_cases.close()