# having a dict for 5 and 10 first getting the 10s done and then go to the 5's only if needed


def lem_chng(bills):
    d={5:0, 10:0, 20:0}
    for i in bills:
        total =i
        if i==5:
            d[i]+=1
        elif i==10:
            d[i]+=1
            if d[5] < 1:
                return False
            else:
                d[5]-=1
        else:
            d[20]+=1
            if d[10] > 0:
                d[10]-=1
                if d[5] >0:
                    d[5] -=1
                else:
                    return False
            elif d[5] < 3:
                return False
            else:
                d[5]-=3
    print(d)
    return True

print(lem_chng([5,5,10,10,20]))