# logic: calculate the number of 1's and 0's so that we eliminate the no of 2 1's and if we have one more 1 then we might need a 0 to make it
# 10 or 11; if not remaining goes to the single bit

# irrespective of the length just considering the last few bits can decide

# running from the first and skipping the two steps if found 1 as not needed to worry about it

def isOneBitCharacter( bits):
    i=0
    len_nums = len(bits)
    while i < len_nums:
        if bits[i]==1:
            if i==len_nums -2:
                return False
            i+=2
        else:
            i+=1

    return True


print(isOneBitCharacter([0,1,0]))