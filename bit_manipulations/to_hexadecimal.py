


def tohex(n):
    if n==0:
        return '0'
    d={10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
    if n<0:
        n += 2**32

    res=''
    while n:
        div = n//16
        rem = n%16
        if rem < 10:
            res= str(rem) + res
        else:
            res = d[rem] + res
        n = div

    return(res)
print(tohex(-530))