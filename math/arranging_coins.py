# can solve by math equaiton n(n+1)/2
import math
def arang_coins(n):
    return int(((math.sqrt(1 + (8 * n)) - 1) / 2))

print(arang_coins(4))