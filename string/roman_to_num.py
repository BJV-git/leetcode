# logic: separate the continuous increasing things and minus all the previous ones to the max

def roman_2_num(s):
    dic={'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500, 'M':1000}
    s+='I'
    slen= len(s)
    summ=0
    res=[]

    i=0
    temp = 0

    while  i < slen-1:

        if dic[s[i]] >= dic[s[i+1]]:
            summ+=dic[s[i]] - temp
            temp=0
        else:
            temp+=dic[s[i]]
        i+=1

    summ+=temp
    return summ

print(roman_2_num('DCXXI'))