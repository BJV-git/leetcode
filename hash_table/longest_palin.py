# logic: is to count the no of even things so that we can form on both sides

def longest_palin(s):
    d={}
    count=0
    flag=0

    for i in s:
        d[i] = d.get(i,0)+1

    for j in d:
        if d[j]%2==1 and flag==0:
            count+=1
            flag=1
        count+= (d[j]//2)*2
    return count


print(longest_palin('aaaAaaaa'))