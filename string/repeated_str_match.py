# logic: we can see that the only changes we can bring is through is by ends
# simply can add so that it is bigger than and see if there

# efficient:
def repeated_str_match(a,b):
    alen = len(a)
    count = 1
    blen = len(b)
    c = a
    i = 1
    f = 0

    min_count=3

    while f <= 2 * blen or min_count>0:

        if c.find(b) != -1:
            return count
        i += 1
        c = a * i
        f = alen * i
        count += 1
        min_count-=1

    return -1

print(repeated_str_match("aaaaaaaaaaaaaaaaaaaaaab","ba"))
