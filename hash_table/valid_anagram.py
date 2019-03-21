
# just need to make sure that, the count is same
# using just one dic

def isanagram(s,t):
    dic={}
    for i in s:
        dic[i] = dic.get(i,0)+1
    for j in t:
        try:
            dic[j] -=1
            if dic[j]==0:
                del dic[j]
        except:
            return False
    return len(dic)==0