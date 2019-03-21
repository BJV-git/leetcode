

def check_alien(words,order):
    d={}
    for i,j in enumerate(order):
        d[j]=i

    lw = len(words)

    for i in range(lw-1):
        f = len(words[i])
        s=len(words[i+1])

        for j in range(max(f,s)):
            left=0
            right= 0

            try:
                left = d[words[i][j]]
            except:
                pass
            try:
                right = d[words[i+1][j]]
            except:
                pass
            if left < right:
                break
            elif left > right:
                return False
            else:
                pass

    return True

print(check_alien(["apple","app"], 'abcdefghijklmnopqrstuvwxyz'))