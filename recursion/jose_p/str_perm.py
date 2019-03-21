# logic: learned (partial) :
# edge cases: if there are repeated letters then need to just remove that only

def str_perm(s):
    len_s = len(s)
    if len_s==1:
        return [s]
    out=[]
    for i in range(len_s):
        temp = s[:i] + s[i+1:]

        out.extend([s[i]+j for j in str_perm(temp)])

    return out

print(len(str_perm('abcda')))

