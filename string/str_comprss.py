# logic: count when encountered new one
# need to compress the arr in place

# can do it from last and insert from the first

def str_compress(arr):
    arrlen = len(arr)
    if arrlen == 1:
        return 1
    result=''

    count=1
    curr=arr.pop()

    while arr:
        temp=arr.pop()
        if temp==curr:
            count+=1
        else:
            if count==1:
                result=curr + result
            else:
                result= curr+str(count)+ result

            curr=temp
            count=1
    if count == 1:
        result = curr + result
    else:
        result = curr + str(count) + result
    for i in result:
        arr.append(i)
    print(arr)
    return len(result)



print(str_compress(["a"]))
