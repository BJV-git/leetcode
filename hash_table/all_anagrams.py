# logic: start counting when we find a match in keys, can start from next to fail
# as before to that, the extra non one makes sure that it fails

# lets maintain a window and do the same as before

def all_anagrms(s,p):
    d = {}
    res = []
    start_index = 0
    lp = 0

    for i in p:
        lp += 1
        d[i] = d.get(i, 0) + 1

    lens = len(s)
    if not s or not p or lp > lens:
        return []

    i = 0
    j = lp - 1

    ref = {i: 0 for i in d}
    while j >= 0:
        if s[j] in d:
            ref[s[j]] = ref.get(s[j], 0) + 1
        j -= 1

    while i < lens - lp + 1:
        if ref == d:
            res.append(i)
        # print(ref)

        if s[i] in d:
            ref[s[i]] -= 1
        if lp + i < lens and s[lp + i] in d:
            ref[s[lp + i]] += 1

        i += 1
    return res

print(all_anagrms('abacbabc', 'abc'))

        # if s[i] in d.keys():
        #     j=i
        #     start_index = j
        #     b=d.copy()
        #     limit = lp
        #     while limit>0:
        #         try:
        #             b[s[j]]-=1
        #             if b[s[i]]<0:
        #                 j-=1
        #                 break
        #         except:
        #             j-=1
        #             break
        #         j+=1
        #         limit-=1
        #
        #
        #     if limit==0 and all([i==0 for i in b.values()]):
        #         # print(start_index)
        #         res.append(start_index)



    #     i+=1
    # return res

