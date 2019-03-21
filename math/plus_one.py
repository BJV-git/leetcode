# logic: just keep on adding the number 1 and if add carry to other too if found 9

def plusOne(digits):


    dlen = len(digits)
    i = dlen-1
    flag = False

    while i >=0 and not flag:
        if digits[i] == 9:
            digits[i] = 0
            i-=1
            continue
        else:
            digits[i] +=1
            flag = True


    if not flag:
        digits.insert(0,1)

    return digits

print(plusOne([9,9,9,9,9,9,9]))