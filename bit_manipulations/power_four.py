# logic learned: num & num-1 is veryfying if it pow od 2

def ispow4(num):
    return num > 0 and num & (num - 1) == 0 and len(bin(num)[3:]) % 2 == 0
