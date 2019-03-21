# logic: lets start from beginning and see if we can find any +, - so that next operation to that is of same priority else,
# lets do that operation first and then perform the addition, so at any point we gonna check the present or the next so constant space


def calculator_str(s):
    s=s.replace(' ','') # cleaned from having the spaces, is this effecient ?
    slen=len(s)

    arr=[]
    one = ['-', '+']
    two = ['*', '/']

    ini=0
    i=0
    while i < slen:
        if not s[i].isalnum():
            arr.append(s[ini:i])
            arr.append(s[i])
            ini = i+1
        i+=1
    arr.append(s[ini:])

    res=[]
    curr=int(arr[0])

    # for i in range(slen):
    #     if s[i].isalnum():
    #         res.append(int(s[i]))
    #     elif




    slen =len(arr)
    if slen ==1:
        return int(arr[0])


    result=int(arr[0])


    def operation( a,oper, b): # s is the op with numbers, actually can also pass just the index
        if oper=='+':
            return int(a)+int(b)
        elif oper=='-':
            return int(a)-int(b)

        elif oper == '*':
            return int(a)*int(b)
        else:
            return int(a)//int(b)


    i=1
    while i < slen: # even numbers will have the numbers and odd has the ops

        if arr[i] in one:
            if i + 2 < slen and arr[i + 2] in two:  # means we need to do teh second the first, in iterative manner
                temp_prev=i
                next = i+2
                temp=int(arr[next-1])
                while next<slen and arr[next] in two:
                    temp = operation(temp, arr[next], arr[next+1])
                    next+=2
                result = operation(result, arr[i], temp) # this shoud be recersive
                i =next
                continue
            else:
                result = operation(result,arr[i], arr[i+1] )
                i+=2
                continue
        else:
            # print("came here")
            result= operation(result,arr[i],arr[i+1])
            i+=2
            continue
        # print(result)
    return  result

print(calculator_str("1+2*5/3/3*5+6/4*2"))