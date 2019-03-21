# logic: as mentioned that 0 is also in the range, first need to eliminate 0 and then form all the possible permutations of the three elements
# and then count the possibilities and return the output
# can take advantage of the ascending order of the sides to decide the triangles.

# learned logic: seen can be done with on2 for loop

# we knew that if the numbers after the digit differences sum less than the number i.e. i then we get n(n-1)/2 till that , so why not repeat that
# while going on

# *********************************************************

# learned : once calculated, no need of calculating again. So, better using the previous results.

def triangleNumber(nums):
    nums.sort()

    nums = list(filter(lambda x: x >0 , nums))
    len_nums = len(nums)
    print(nums)
    if len_nums >= 3:
        possible_traingles =0
        for i in range(len_nums-2):
            k = i+2
            for j in range(i+1,len_nums):
                while k < len_nums and nums[i] + nums[j] > nums[k]:
                    k+=1
                possible_traingles += k-j-1

        return possible_traingles
    else:
        return 0

print(triangleNumber([0,0,0]))

# # logic: as mentioned that 0 is also in the range, first need to eliminate 0 and then form all the possible permutations of the three elements
# # and then count the possibilities and return the output
# def triangleNumber(nums):
#     len_nums = len(nums)
#     sides = {}
#     num_set = sorted(list(set(nums)))
#
#     len_set = len(num_set)
#     for i in range(len_set - 2):
#
#
