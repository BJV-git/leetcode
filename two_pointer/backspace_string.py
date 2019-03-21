


def bkspc_str(S,T):

    lens = len(S)
    lent = len(T)


    i=0
    while i < (lens):
        if S[i]=='#': # start while loop
            start_r  = i

            while (start_r < lens and S[start_r]=='#'):
                start_r+=1
            right = start_r
            left = max((i - (start_r - i)),0)
            S = S[:left] + S[start_r:]
            lens = len(S)
            i=0

        i+=1

    i=0
    while i < (lent):
        if T[i]=='#': # start while loop
            start_r  = i

            while (start_r < lent and T[start_r]=='#'):
                start_r+=1
            right = start_r
            left = max((i - (start_r - i)),0)
            T= T[:left] + T[start_r:]
            lent = len(T)
            i=0

        i+=1
    print(S,T)


    return S==T

print(bkspc_str("ab##","cd##"))