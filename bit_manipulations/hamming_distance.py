


def hamm_dis(x,y):
    return bin(x ^ y).count('1')
    
    x = str(bin(x)[2:])
    y = str(bin(y)[2:])

    lx = len(x)
    ly = len(y)

    if lx > ly:
        y = '0'*(lx-ly)+y
    elif lx < ly:
        x = '0'*(ly-lx)+x

    c=0
    for i in range(max(lx,ly)):
        if x[i]!=y[i]:
            c+=1
    return c



print(hamm_dis(1,4))
