
import re
def rev_vowels(s):
    slen = len(s)
    v = set(['a', 'e', 'i', 'o', 'u'])
    if slen == 1 or not any(i.lower() in v for i in list(s)):
        return s

    s = list(s)
    start = 0
    end = slen - 1
    while start <= end:
        if not s[start].lower() in v:
            while start <= end and not s[start].lower() in v:
                start += 1
        if not s[end].isalpha():
            while end >= start and not s[end].lower() in v:
                end -= 1

        if s[start].lower() in v and s[end].lower() in v:
            s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    return (''.join(s))

print(rev_vowels('leetcode'))