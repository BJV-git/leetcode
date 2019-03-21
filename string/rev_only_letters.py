
import re
def reverse_letters(s):
    slen = len(s)
    if slen==1 or not any(i.isalpha() for i in list(s)):
        return s

    s = list(s)
    start =0
    end = slen-1
    while start <= end:
        if not s[start].isalpha():
            while start <=end and not s[start].isalpha():
                start+=1
        if not s[end].isalpha():
            while end >= start and not s[end].isalpha():
                end-=1
        if s[start].isalpha() and s[end].isalpha():
            s[start], s[end] = s[end],s[start]
        start+=1
        end-=1



    return (''.join(s))


print(reverse_letters("7_28]"))