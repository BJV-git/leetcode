# can use a while loop when found a zero and skip to the next after replacement


def move_0(nums):
    zeros = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zeros] = nums[zeros], nums[i]
            zeros += 1

    return nums

print(move_0([0,1,0,3,12]))