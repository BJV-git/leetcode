


def jewels_stones(J,S):

    jew=set(J)
    print(jew)
    count=0
    for i in S:
        if i in jew:
            count+=1

    return count

print(jewels_stones('aA', 'aAAjjjj'))