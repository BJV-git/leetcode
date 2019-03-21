
def reverse(self, x):

    if x >=0:
        x = int(str(x)[::-1])
    else:
        x = abs(x)
        x = -int(str(x)[::-1])
    if not -2147483648 <= x <= 2147483647:
        return 0
    else:
        return x
