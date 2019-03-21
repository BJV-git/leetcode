

def find_single(arr):
    dic = {}
    for i in arr:
        dic[i] = dic.get(i, 0) + 1
        if dic[i] == 2:
            del dic[i]
    return (list(dic.keys())[0])