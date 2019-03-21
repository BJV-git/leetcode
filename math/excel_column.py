# logic: just have a dict mul and add
# its just a numbers system in 26 value that's it
# logic is same as how we convert from one number system to other


# got the logic: used the general rule of the division multi times, when encountered 0 -1 the remaining n

def no_excel(n):
    out=''
    dic={1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K', 12:'L', 13:'M', 14:'N', 15:'O', 16:'P', 17:'Q', 18:'R', 19:'S', 20:'T', 21:'U', 22:'V', 23:'W', 24:'X', 25:'Y', 26: 'Z'}
    while n >0:
        rem = n%26
        n = n // 26
        if rem == 0 :
            n -=1
            out = 'Z' + out
        else:
            out = dic[rem] + out
    return out


print(no_excel(260))