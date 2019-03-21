# logic : just add the numbers and minus from the max and n(n-1)/2
# also just need to see the size

def missingNumber(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        if nums[0] == 0:
            return 1
        if nums[0] == 1:
            return 0
        else:
            return nums[0] + 1

    total = 0
    maxi = 0
    mini = 1

    for i in nums:
        total += i
        maxi = max(maxi, i)
        mini = min(mini, i)
    summ = ((maxi * (maxi + 1)) / 2) - total

    if mini == 1:
        return 0
    if summ == 0:
        return maxi + 1

    else:
        print('here')
        return summumm