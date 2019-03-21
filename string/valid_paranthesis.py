

def valid_paranthesis(s):

    open = set(['{', '(', '['])
    close = set(['}', ']', ')'])

    dic = {'}': '{', ')': '(', ']': '['}
    if len(s) % 2 == 1:
        return False

    stack = []

    for i in s:

        if i in open:
            stack.append(i)

        else:
            try:
                if stack.pop() != dic[i]:
                    return False
            except:
                return False

    return not stack
print(valid_paranthesis('(('))