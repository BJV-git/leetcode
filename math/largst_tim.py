# logic: atleast 0-5 there shoudl be 2 to fill the left of both hours and minutes

# just add one and more till 5
# only thing need to make sure is if one fails do we have another is to be checked
# learned: check for all the permutations

import itertools
def largst_tim(a):
    # print(["%d%d:%d%d" % t for t in itertools.permutations(a) if t[:2] < (2, 4) and t[2] < 6] or [""])
    r=[]

    i=2
    while i>=0:
        # print(i)
        res=''
        m=''
        b = a.copy()
        if i in b:
            res+=str(i)
            b.remove(i)
            if res == '2':
                j=3
                while j>=0:
                    if j in b:
                        res+=str(j)
                        # print(res)
                        b.remove(j)
                        break

                    j-=1
                if len(res)==1:
                    r.append('')
                    i-=1
                    continue
            else:
                maxi = max(b)
                res+= str(maxi)
                # print(res)
                b.remove(maxi)

            # now the minutes

            k=5
            while k >=0:
                if k in b:
                    m+=str(k)
                    # print(m)
                    b.remove(k)
                    break
                k-=1

            if not m:
                r.append('')
                i-=1
                continue
            else:
                # print(res+':'+m+str(b[0]), 'here')
                r.append(res+':'+m+str(b[0]))
        else:
            r.append('')

        i -= 1

    return max(r)
# print(largst_tim([4, 2, 4, 4]))
print(largst_tim([2,0,6,6]))






    # r=[]
    # res=''
    # m=''
    # a.sort()
    #
    # # for first
    #
    # i=2
    # while i>=0:
    #     if i in a:
    #         res+=str(i)
    #         a.remove(i)
    #         break
    #     i-=1
    #
    # if not res:
    #     return ''
    #
    # if res=='2':
    #     i=3
    #     while i>=0:
    #         if i in a:
    #             res+=str(i)
    #             a.remove(i)
    #             break
    #         i-=1
    #     if len(res)==1:
    #         return ''
    # else:
    #     maxi = max(a)
    #     res+= str(maxi)
    #     a.remove(maxi)
    #
    # # the hours are done , now time to go for the minutes
    #
    #
    # i=5
    # while i >=0:
    #     if i in a:
    #         m+=str(i)
    #         a.remove(i)
    #         break
    #     i-=1
    #
    # if not m:
    #     return ''
    # else:
    #     return res+':'+m+str(a[0])

