

def wrd_ptrn(p, s):
    t=s.split(' ')
    print(t)
    lenp = len(p)

    if lenp!=len(t):
        return False

    dic={}
    se = set()
    # with out replacing the original we can use the dic refrenece
    for i  in range(lenp):
        print(dic)
        if p[i] in dic:
            if dic[p[i]] == t[i]:
                continue
            else:
                return False

        if t[i] in se:
            return False
        dic[p[i]] = t[i]
        se.add(t[i])

    return True

print(wrd_ptrn("abba", 'dog cat cat mice'))