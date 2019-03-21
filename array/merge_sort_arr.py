# as we need to merge into the first one,
# we can first add the nums in second, then sort in place


def merge(nums,n,arr,a):
    i = -1
    while arr:
        a = arr.pop()
        nums[i] = a
        i -= 1
    nums.sort()
