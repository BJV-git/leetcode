


def game(ops):
    stack = []
    for i in ops:
        if '-' in i:
            stack.append(int(i))
        elif i.isnumeric():
            stack.append(int(i))
        elif i == 'C':
            stack.pop()
        elif i == 'D':
            stack.append(2*stack[-1])
        else:
            total = stack[-1] + stack[-2]
            stack.append(total)
    return sum(stack)
print(game(["5","-2","4","C","D","9","+","+"]))