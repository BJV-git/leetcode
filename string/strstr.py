# while comparing better use two pointers so that we can move things twice fast

def strstr(a,b):
    if not a and not b:
        return 0
    if not a:
        return -1
    if not b:
        return 0

    alen = len(a)
    bcount = len(b)
    # flag = 0
    # count = 0
    i=0
    while i < alen:
        if a[i] ==b[0]: # start checking
            mid = i+(bcount//2)
            start=i
            end=i+bcount-1
            while start <= mid and end >= mid and end < alen and a[start] == b[start-i] and a[end]==b[end-i]:
                start+=1
                end-=1
            print(start)
            print(end)
            if start > end:
                return i

        i+=1

    return -1


print(strstr('babba','bbb'))