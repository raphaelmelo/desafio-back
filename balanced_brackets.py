#!/bin/python3

# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING brackets as parameter.
def isBalanced(brackets):
    stack = []
    open_brackets = ["[","{","("]
    close_brackets = ["]","}",")"]

    for i in brackets:
        if i in open_brackets:
            stack.append(i)
        elif i in close_brackets:
            pos = close_brackets.index(i)
            if ((len(stack) > 0) and # verifico se a quantidade de items é maior que 0
                (open_brackets[pos] == stack[len(stack)-1])): # e se a quantidade de item da close_brackets é a mesma da open_brackets
                stack.pop()
            else:
                return "NO"
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':

    t = int(input().strip())

    results = []
    for t_itr in range(t):
        brackets = input()

        results.append(isBalanced(brackets))

    print(*results, sep='\n')
