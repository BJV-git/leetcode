
def reverse_II(s,k):
    slen = len(s)
    result=''

    limit = (slen//(2*k))*2*k

    remain = slen%(2*k)

    i=0
    while i < limit:
        try:
            result += s[i:i+k][::-1] + s[i+k:i+2*k]
        except:
            pass
        i += 2*k

    return result+s[limit:limit+k][::-1] + s[limit+k:]
print(reverse_II("abcdef", 2))