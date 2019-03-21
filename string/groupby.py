# logic: have dicts of length 1 to 20 now can append and see if exists else count +=1

def groupby(arr):
    dic = {i:[] for i in range(1,21)}
    groups=0

    for i in arr:
        odd=''
        even=''
        final=''
        ilen = len(i)
        for j in range(ilen):
            if j%2==0:
                even+=i[j]
            else:
                odd+=i[j]

        final = ''.join(sorted(odd))+''.join(sorted(even))

        if any(final in i for i in dic[ilen]):
            continue
        else:
            groups+=1
            dic[ilen].append([final])

    return groups

print(groupby( ["abcd","cdab","adcb","cbad"]))
