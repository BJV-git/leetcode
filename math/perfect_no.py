# logic: can use the shortcut methods mentioned and then we go for normal stuff
# i.e. we see if every things is fact or not and then add them up

# in normal process lets keep track of left where we can stop early

def perf_no(n):

    i = 2
    t = 0
    while t < n:

        t = (2**(i-1)) * ((2**i)-1)
        if t == n:
            return True
        i+=1
    return False

print(perf_no(2976221))