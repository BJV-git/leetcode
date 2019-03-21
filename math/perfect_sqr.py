# logic: with out using the sqrt function
# so just write the fucntion of sqrt and do it


def isPerfectSquare( num):
    def sqrt(n):
        if n < 2:
            return n
        l = 0
        r = n

        while l <= r:
            mid = (l + r) // 2
            if mid ** 2 == n:
                return mid
            if mid ** 2 < n < (mid + 1) ** 2:
                return mid

            elif mid ** 2 > n:
                r = mid + 1
            else:
                l = mid - 1

    s = sqrt(num)
    return s ** 2 == num


print(isPerfectSquare(0))