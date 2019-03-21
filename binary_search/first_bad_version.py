# have the start in the prev and change the mid with the last


def frst_bd_vrsn(n, b):
    start = 1
    end = n

    def isBadVersion(n):
        if n==b:
            return True
        else:
            return False

    def bin(start,end):

        if isBadVersion(start):
            return start
        if start+1 ==end:
            if isBadVersion(start):
                return start
            if isBadVersion(end):
                return end

        elif isBadVersion((start+end)//2):
            return bin(start, (start+end)//2)
        else:
            return bin((start+end)//2, end)

    return bin(1,n)

print(frst_bd_vrsn(10,5))