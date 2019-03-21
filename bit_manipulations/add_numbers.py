# learned: & means

def add(a,b):

    max = 0x7FFFFFF
    min = 0x8000000

    mask =0xFFFFFFFF

    while b !=0:
        a,b = (a^b) & mask , ((a&b) << 1) & mask
    return a if a <= max else ~(a^mask)

print(8&1100)