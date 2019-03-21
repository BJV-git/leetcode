# logic: with out usign loop means we cna just convert into binary to see if there is only just one 1

def ispow2(num):
    return num > 0 and str(bin(num)[2:]).count('1') == 1