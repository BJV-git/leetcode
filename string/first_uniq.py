# logic: count dict and see which has 1s to see the first of them getting encountered and return

# can have tuples with the letter and count, sort things so that if one return else -1
import collections
def first_uniq(s):
    dic= collections.OrderedDict()
    for i in s:
        dic[i] = dic.get(i,0)+1
    for j in dic:
        if dic[j]==1:
            return j
    return -1
