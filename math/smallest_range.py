 # the logic is to make sure we minimize the difference


# can we do as find the min diff and hwo far we can reach to the 0 -

# the min and max are to be considered so need to consider them

import sys
def smallest_range(arr,k):
    if len(arr) < 2: return 0
    return max(max(arr)-k -(min(arr)+k),0)

print(smallest_range([3,1,10], 4))