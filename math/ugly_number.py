# logic: rule is that, we need to find that, if its only factors are 2 and 3 so just divide by 2,3 and 5 so that if reminder is zero


def isUgly(num):
    if num == 0:
        return False
    while num % 5 == 0:
        num = num // 5

        # print(num)
    while num % 3 == 0:
        num = num // 3
        # print(num)

    while num % 2 == 0:
        num = num // 2
        # print(num)
    if num == 1:
        return True
    else:
        return False
