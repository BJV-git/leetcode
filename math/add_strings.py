# logic: just  have the total and factor to get numtiplied

# better to use the dict, at two times
# instead of reverse lets get length

def addstr(x,y):

    dic = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    fact = 1
    total = 0
    t = 0

    lenx = len(x)
    leny   =len(y)

    for i in range(lenx-1, -1,-1):
        total += fact * dic[x[i]]
        fact = fact * 10

    fact = 1

    for j in range(leny-1, -1,-1):
        t += fact * dic[y[j]] # with out using the int converting function
        fact = fact * 10

    result=''

    # the idea is to see how we can map the things and better to have one more dict
    dic = {j:i for i,j in dic.items()}
    fact=10
    summ = t+total
    n=1

    if summ==0:
        return '0'

    while summ!=0:
        n = (summ)%fact
        result = dic[n] + result
        summ//=10
    return result

print(addstr("0","0"))