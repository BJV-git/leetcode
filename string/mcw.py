

import re
import collections

def mcw(para, ban):
    ban = [i.lower() for i in ban]
    pattern = r'(\w+)'
    l = [i for i in re.findall(pattern, para) if i.lower() not in ban]
    dic={}
    for i in l:
        dic[i.lower()] = dic.get(i.lower(),0)+1

    maxi=0
    ret=''
    for i in dic:
        if dic[i] > maxi:
            ret = i
            maxi=dic[i]
    return ret

print(mcw("Bob hit a ball, the hit BALL flew far after it was hit.", ['hit']))
print()