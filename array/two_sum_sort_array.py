# can use dic
# position does matter while keeping into the dictionary

def find(nums, target):
    d={}
    for i,j in enumerate(nums):

        t=target-j
        if t in d and d[t]!=i+1:
            return [d[t], i+1]
        d[j] = i + 1
    return None

print(find([2,2,11,15],100))