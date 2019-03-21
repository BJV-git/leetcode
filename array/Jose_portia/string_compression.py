# logic: simple is to count and just join

def string_compression(a):
    len_s = len(a)
    if len_s ==1:
        return a+str(1)
    cur=a[0]
    cur_pos=0
    res=''
    for i in range(1,len_s):

        if a[i] != cur:
            res = res+cur+str(i-cur_pos)
            cur=a[i]
            cur_pos=i
    # checking for the last element

    if cur == a[len_s-1]:
        res = res+cur+str(len_s-cur_pos)
    else:
        res = res+cur+str(1)

    return res

print(string_compression('AAaaa'))