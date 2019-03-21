



def shrtst_compltng_wrd(lp,words):
    d = {}

    res = ''
    flag = 0
    seen=[]

    for i in lp:
        if i.isalpha():
            d[i.lower()] = d.get(i.lower(), 0) + 1
    for word in words:
        e = d.copy()
        for letter in word:
            if letter.lower() in d:
                e[letter.lower()]-=1


        if all(i<=0 for i in e.values()):
            if flag == 0:
                res = word
                flag = 1

            if len(res) > len(word):
                res = word

    return res

print(shrtst_compltng_wrd("GrC8950",
["measure","other","every","base","according","level","meeting","none","marriage","rest"]))

# print(['a','b','b'] in ['a','b','b','b','c'])