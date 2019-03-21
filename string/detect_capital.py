
def detect_cap(word):
    wlen = len(word)
    flag=0
    if wlen == 1:
        return True

    i=1
    if word[0].isupper() and word[1].isupper():
        flag=1
    while i < wlen:

        if flag==1 and word[i].islower():
            return False
        if flag==0 and word[i].isupper():
            return False
        i+=1
    return True

print(detect_cap('mL'))