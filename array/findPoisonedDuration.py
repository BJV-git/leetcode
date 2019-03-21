# logic:  start from 1 and compare the limit and current to add span
def findPoisonedDuration(timeSeries, duration):

    span=0
    if duration <=0:
        return 0
    elif timeSeries:
        prev_pos = timeSeries[0]
        limit = prev_pos + duration - 1
        for i in timeSeries[1:]:
            if (i > limit):
                span+=duration
            else:
                # print("i",i)
                # print("prev_pos", prev_pos)
                span+= (i-prev_pos)
                # print(span)
            limit=i+duration-1
            prev_pos=i
    else:
        return 0
    # print(span)
    return span+duration



print(findPoisonedDuration([1,2,3,4,5],5))