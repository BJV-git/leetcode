# logic: we can just see for the raise and then get the decrease poiont, this shoud be max and repeat

# flag means in search
def best(prices):
    i=0
    l = len(prices)
    flag=0
    profit=0

    while i+1 < l:
        if prices[i] < prices[i+1]:
            buy =  prices[i]
            temp = i+1
            prev = buy
            while temp+1 < l and prices[temp] < prices[temp+1]:
                temp+=1

            print(i, temp)


            if temp < l  and prices[temp-1] >= buy:
                profit += prices[temp] - buy

                i=temp+1
                continue

        i+=1
    return profit

print(best([1,2,3,4,5]))