# lets have a max
# having the prev, we can say if the prev == curr then we gotta move forward else just be cool

# so its like stagging at point where we wanna keep the next and move on the otehr any ways move with some  indicator

import sys
def move_dups(nums):
    prev =  sys.maxsize
    count=0
    for i,j in enumerate(nums):
        if j!=prev:
            nums[i], nums[count] = nums[count], nums[i]
            prev=j
            count+=1

    print(nums)
    return count

print(move_dups([1,1,2]))