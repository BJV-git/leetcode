# convert to binary
# diff between the first and last one

# consecutive means just the before one

def bin_gap(n):
    t = str(bin(n)).replace('0b','')
    print(t)
    first_cord=None
    last_cord=None
    first=0
    lent = len(t)
    last = lent-1
    stop=0


    while (first<lent or last>0) and stop < 2:
        if t[first]=='1' and first_cord is None:
            first_cord=first
            stop+=1
        if not first_cord:
            first+=1
        if t[last]=='1' and not last_cord:
            last_cord = last
            stop+=1
        if not last_cord:
            last-=1
    print(first_cord, last_cord)
    return last_cord - first_cord


# n = bin(N)[2:]
# dic = {}
# longest = 0
#
# for i in range(len(n)):
#     if n[i] == '1':
#         if 1 in d:
#             val = i - d[1]
#             longest = max(longest, val)
#         d[1] = i
# return longest

print(bin_gap(22))