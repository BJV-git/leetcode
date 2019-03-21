# logic : carry the common thru iteration and finally will be the common of all
# at any time if its null return 0, why waste time

def longest_prefix(arr):
    arrlen= len(arr)

    if arrlen==0:
        return ''
    if arrlen==1:
        return arr[0]

    common = arr[0]

    for i in range(1,arrlen):
        print("i",i)
        temp=''
        comlen=len(common)
        for j in range(comlen):
            try:
                if arr[i][j] == common[j]:
                    temp = temp+common[j]
                else:
                    common = temp
            except:
                common = temp

        if not common:
            return ''

    return common

print(longest_prefix(["dog","racecar","car"]))