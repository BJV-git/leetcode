# logic: even though the chars are different their respective count shoudl be equal
# i.e. their sorted order should be equal

# the goal is to check if there can be a one to one map and in order

# leanred from test case: aa and ab, Flase, so we need to insert the mapping for each element

def iso_str(s,t):
    lent = len(t)
    lens = len(s)
    if lens!=lent:
        return False

    dic={}
    se = set()
    # with out replacing the original we can use the dic refrenece
    for i  in range(lent):
        print(dic)
        if s[i] in dic:
            if dic[s[i]] == t[i]:
                continue
            else:
                return False

        if t[i] in se:
            return False
        dic[s[i]] = t[i]
        se.add(t[i])


    return True

print(iso_str('baa','cfa'))