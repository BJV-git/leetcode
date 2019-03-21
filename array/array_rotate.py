# def rotate(arr,k):
#     part1 = arr[-3:]
#     print(part1)
#     part2 = arr[:k+1]
#     print(part2)
#     print(part1+part2)


def rotate(arr,k):
    if arr:
        len_arr = len(arr)
        if len_arr ==1 or k%len_arr==0:
            print( arr)

        else:
            k = k%len_arr
            print( arr[-k:] + arr[:len(arr)-k])

rotate([1,2,3,4,5,6,7], 3)
