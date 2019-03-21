

def hapy_no(n):
    if n < 0:
        return False
    seen = set()
    while True:
        print(n)
        total = 0
        for i in str(n):
            total += int(i) ** 2
        if total ==1:
            return True
        if total in seen:
            return False
        else:
            n = total
            seen.add(total)


print(hapy_no(1111111 ))