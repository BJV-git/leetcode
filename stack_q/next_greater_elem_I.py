# instead of array for the first one

# logic: he is looking for a peak and then seeing for how many numbers he can assign that, and next repeat

def next_greater(findNums, nums):
    d = {}
    st = []
    ans = []

    for x in nums:
        while len(st) and st[-1] < x:
            d[st.pop()] = x
        st.append(x)
    for x in findNums:
        ans.append(d.get(x,-1))
    return ans


print(next_greater([5,3,2,1],[5,4,3,2,1,6]))