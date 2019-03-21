# logic: set flag and count

def no_of_seg(s):

    s= s.strip()

    count=0
    flag=0

    slen=len(s)
    if slen ==0:
        return 0

    i=0
    while i < slen:
        if s[i].isspace():
            flag=0
        if flag==0 and not s[i].isspace():
            count+=1
            flag=1

        i+=1
    return count
print(no_of_seg('Hello'))