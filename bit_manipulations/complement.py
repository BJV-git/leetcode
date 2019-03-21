

def com(num):
    num = str(bin(num)[2:])
    num = ''.join('0' if i == '1' else '1' for i in num)
    return int(num, 2)