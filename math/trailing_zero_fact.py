# hwo: ???


import math
def taril_zero(n):
    cnt = 0
    while n >= 5:
        n //= 5
        cnt += n
    return cnt
