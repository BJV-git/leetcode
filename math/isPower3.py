

def ispower3(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    temp = 3
    while True:
        if temp > n:
            return False
        if temp == n:
            return True
        temp = temp * 3