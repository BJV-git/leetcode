# logic: if in left one just add up in to stack and then pop when seen the opposites
# during the interviews we need to talk about how we are approaching the problem like at the point we know its false
# are we quitting the porb or doing unnecesary checks and so on

def balanced_check(s):
    s_len=len(s)
    maps={')':'(', ']':'[', '}':'{'}

    if s_len > 1:
        stack=[]
        for i in s:
            if i in ['(','{','[']:
                stack.append(i)
            else:
                try:
                    a = stack.pop()
                    if a == maps[i]:
                        pass
                    else:
                        return False
                except:
                    return False
        return True


    return False

print(balanced_check('()[]{([[[]]])}'))
print(balanced_check('()()]}'))
