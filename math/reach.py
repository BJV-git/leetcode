# logic: as on nth step we make n dis on nth move,

# found pattern: if I get the nearest number of sum of n, based on distance can tell teh number of moves min
# if teh nearest sigma n is even, dis: odd = 1, even = 3
#  else dis: odd: 2 , even: 1

def reach(target):
    target = abs(target)
    nearest = int((((1 + 8 * target) ** 0.5) - 1) / 2)
    summ = (nearest * (nearest + 1)) / 2
    diff = target - summ
    if diff == 0:
        return nearest
    elif nearest % 2 == 0:  # even
        if diff % 2 == 0:
            return nearest + 3
        else:
            return nearest + 1
    else:
        if diff % 2 == 0:
            return nearest + 1
        else:
            return nearest + 2
