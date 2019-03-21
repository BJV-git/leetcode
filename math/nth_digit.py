# logic: not using the str join method, so
# its about first minus the 9 and then divide by 20 each time, and so on

# lets do minus till we find the greater one
# and divide by the inetger to add and the rem is the rem-1th interger to return

def nthdigit(n):
    if n <= 9:
        return n

    fact = 10
    i = 2
    prod = 9
    while prod <= n:
        n = n - prod
        prod = 9 * i * fact
        i += 1
        fact *= 10
    digits = i - 1  # is the number of digits
    start = 10 ** (digits - 1)
    add = n // digits
    start += add

    rem = n % digits
    if rem == 0:
        return (add - 1) % 10

    return int(str(start)[(n % digits) - 1])


print(nthdigit(25))