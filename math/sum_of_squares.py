# logic: go until can find the numebrs till n
# again see if we can find the number of sum

def ifsq(n):

    seen = set()
    i=1
    while i**2 <n :
        target = n - (i**2)
        if target in seen:
            return True
        seen.add(i**2)
        i+=1
    return False
