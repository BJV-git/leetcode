# logic: to use bs to find the nearest heater and append the diff

def radius(houses, heaters):
    lhe = len(heaters)
    heaters.sort()
    houses.sort()
    res=[]

    def bin(start, end):
        mid=0
        while start<=end:
            mid = (start+end)//2
            if heaters[mid] == target:
                return heaters[mid]
            elif mid+1 <= end and abs(heaters[mid] - target) < abs(heaters[mid+1] - target):
                end = mid
            else:
                start = mid + 1
        return heaters[mid]

    for i in houses:
        target = i
        if lhe ==1:
            closest = heaters[0]
        else:
            closest = bin(0,lhe-1)
        res.append(abs(target - closest))

    print(res)

    return max(res)




print(radius([282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923],
[823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]))