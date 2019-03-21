# logic: we can distribute the same kind of many number to bro adn then different to sis
# the max it can get is total/2, if not there then less

# if more but the max is only

def dist_cand(candies):

    kind = len(set(candies))
    lc = len(candies)
    half = lc//2

    if kind <= half:
        return kind
    else:
        return half