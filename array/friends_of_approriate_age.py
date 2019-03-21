# logic: simple is to store already calculated values and then for each age find all others possibilities - time out so

# better: sort the given things and for each person better to find the range and then calculate the range and terminate when
# exceeding the limit

# based on conditions no need to check the upper limit, only to look for lower limit unless age > 100

# can have a start and end window. Now, all need to be done is that need to move the ends according to the person and just adding the ranges.
# learned from the possible triangles

def numFriendRequests(ages):
    len_ages = len(ages)
    summ=0
    if len_ages==1:
        return 0
    else:
        ages.sort()
        print(ages)
        start=end =0
        for i in range(len_ages):
            limit = 0.5 * ages[i] + 7
            while ages[start] <= limit:
                start+=1

            while end < len_ages-1 and ages[end+1] == ages[i] :
                end+=1

            print("start for {0} is {1}".format(i, start))
            print("end for {0} is {1}".format(i, end))
            print("summ", summ)
            print("")

            if end-start>0:
                summ += end -start # -1 is for the person himself
            # print("summ", summ)
    return summ

print(numFriendRequests([108,115,5,24,82]))

            # while i < len_ages:
        #     # if ages[i] <= 100: # no need to check for right loop
        #     limit = 0.5*ages[i]+7
        #     j = i-1
        #     age = ages[i]
        #
        #     while  j >= 0 and ages[j] > limit and  ages[j] <= age: # Not to go beyond the limits of input
        #         # print("i",i)                                    # should be > limit
        #         # print("j",j)                                    # and finally the upper limit is that <= ages
        #         # print("on left side", ages[j], limit)
        #         summ+=1
        #         j-=1
        #
        #     j=i+1
        #
        #     while j < len_ages and ages[j] > limit and ages[j] <= age:
        #         # print("i", i)
        #         # print("j", j)
        #         # print("on right side", ages[j], limit)
        #         summ+=1
        #         j+=1
        #     i+=1
        # return summ

        #
        # multi = {z:0 for z in [i for i in ages if ages.count(i)>1]}
        # # print(multi)
        # summ=0
        # for j in range(len_ages):
        #     age=ages[j]
        #     # print("age",age)
        #     if age in multi.keys():
        #         if multi[age] > 0:
        #             summ+= multi[age]
        #         else:
        #             multi[age] = sum([1 for i in range(len_ages) if j!=i and not((ages[i] <= 0.5*age + 7) or(age < ages[i]) or (ages[i] > 100 and age < 100 ))  ])
        #             summ+=multi[age]
        #     else:
        #         summ+=sum([1 for i in range(len_ages) if j!=i and not((ages[i] <= 0.5*age + 7) or(age < ages[i]) or (ages[i] > 100 and age < 100 ))])
        #
        # return summ