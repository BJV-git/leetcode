


def guessno(n,b):

    def guess(n):
        if n==b:
            return 0
        elif n > b:
            return 1
        else:
            return -1

    start = 1
    end = n

    while start <= end:
        mid = (start + end) // 2
        g = guess(mid)
        if g == 0:
            return mid
        elif g == -1:
            end = mid - 1
        else:
            start = mid + 1

print(guessno(10,5))