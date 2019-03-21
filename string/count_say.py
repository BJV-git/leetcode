# logic: just count the previous str unitl we face new one and append the count to current digit and output

# TypeError: Can't convert 'int' object to str implicitly

def count_and_say(n):


    opt='1'

    for i in range(1,n):
        output=''
        curr = opt[0]
        count=0
        slen=len(opt)

        # print("opt",opt, "curr", curr)
        for j in range(slen):
            if j <= slen and opt[j]==curr:
                count+=1
            else:
                output = output + str(count) + curr
                curr=opt[j]
                count=1

        opt = output+str(count) + curr

    return opt

print(count_and_say(7))