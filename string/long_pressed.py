# logic: can use dict and see if nay goes below 0 so flase
# but this woudn't get the order so better to compress and then decide

# learned that at that point of time the dict count has to be more or equal

def long_pressed(name, typed):

    i=0
    j=0
    nlen= len(name)
    tlen=len(typed)

    while j < tlen:
        if typed[j] == name[i]:
            i+=1
        j+=1
    print(i)

    return i > nlen-1
print(long_pressed("pyplrz","ppyypllr"))
    # one=''
    # two=''
    # curr=''
    # for i in name:
    #     if curr!=i:
    #         one+=curr
    #         curr=i
    # curr=''
    #
    #
    # for j in typed:
    #     if curr != j:
    #         two+=curr
    #         curr=j
    # print(one)
    # print(two)
    #
    # dic={}
    # for i in typed:
    #     dic[i] = dic.get(i,0)+1
    #
    # for j in name:
    #     try:
    #         dic[j] = dic[j]-1
    #         if dic[j] < 0:
    #             return False
    #     except:
    #         return False
    # return True and one==two

# print(long_pressed("kpufanyrqqmtgxhyycltlnusyeyyqygwupcaagtkuqkwamvdsi","kpuufaanyrqqqmttggxxhyyyycclttllnusyeyqqyggwuuppccaaaggtkkuuqkwwamvvddsii"))
