# the index sum matters as if like a best nearest restaurant for both of them

import collections
import sys
def findRestaurant(l,m):
    res=[]
    d={}
    for i,j in enumerate(l):
        d[j]=[i]
    for i,j in enumerate(m):
        if j in d:
            d[j].append(i)
        else:
            d[j]=[i]
    # print(d)

    d={i:sum(d[i]) for i in d if len(d[i])==2}

    # print(d)

    mini=sys.maxsize

    for i in d:

        if mini > d[i]:
            mini =d[i]
            res=[]
            res.append(i)
            continue
        if d[i]==mini:
            res.append(i)
    # print(res,'res')
    return res

print(findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],
["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))