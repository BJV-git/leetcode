# logic: pattern is found in by adding first all the elements from left to right and find the largest element index
# can do the same by reversing direction: the result is the sum between the indices

# working for even single element and no element
# learned: just check summ till that point and see if its greater than current number, if so swap and start new sum

def longest_continuous_sum(arr):
    len_arr=len(arr)

    summ=0
    temp=0

    start=0
    end=len_arr-1

    for i in range(len_arr):
        temp+=arr[i]

        if temp> summ:
            start=i
        summ=temp

    summ=0
    temp = 0
    # start-=1

    for i in range(len_arr-1,-1,-1):
        temp += arr[i]

        if temp > summ:
            end = i
        summ = temp
    # end-=1

    print("start", start, "end ", end)



    return sum(arr[end:start+1]) # or can return the max of two

print(longest_continuous_sum([-2,-3,4,-1,-2,1,5,-3]))
print(longest_continuous_sum([1,2,-1,3,4,10,10,-1]))
print(longest_continuous_sum([1,2,-1,3,4,-1]))
print(longest_continuous_sum([-1,1]))


