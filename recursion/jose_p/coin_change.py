def coin_change(n, arr ):
    target = n
    summ=0
    arr.sort()
    prev = 0
    curr = arr.pop()

    while target !=0:
        if target >= curr:
            summ += target//curr
            target = target%curr
            prev = curr
            try:
                curr = arr.pop()
            except:
                pass
        else:
            target+=prev
            summ-=1

    return summ

print(coin_change(10,[5,1,10]))