


def find_ins(nums, target):
    i = 0
    ans = 0
    while True:
        try:
            if nums[i] >= target:
                ans = i
                break

            i += 1
        except:
            break
    return i