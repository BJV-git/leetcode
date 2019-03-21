# when ever we assigned a cookie to the bidda, we need to move forward so that it might nto get assigned again to the other person


def assign(g,s):
    g.sort()
    s.sort()

    print(g)
    print(s)

    i=0
    j=0
    limit = len(s)
    lim = len(g)
    count=0

    while j < limit and i < lim:
        while j < limit and s[j] < g[i]:
            j+=1
        if j < limit and s[j] >= g[i]:
            count+=1
            j+=1
        i+=1

    return count

print(assign([1,2,3],[3]))