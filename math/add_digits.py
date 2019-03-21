

def add_digits(n):
    if n == 0:
        return 0
    rem = n % 9
    if rem == 0:
        return 9
    else:
        return rem