# logic: can first go through the strings, to count the alphabest using isalpha()
# now that the dict is updated we can just subtract the things to see of any > 1 count exist

# can we check with the length and make it fast? yes may be by eliminating the spaces and just counting the letters

# learned convert to lower


# simple python way of soplution

# def isAnagram(a,b):
#     a = a.replace(' ','').lower()
#     b = b.replace(' ', '').lower()
#
#     return sorted(a) == sorted(b)

def isAnagram(a,b):
    count={}

    for i in a:
        if i.isalpha():
            count[i.lower()] = count.get(i.lower(),0)+1
    for i in b:
        if i.isalpha():
            try:
                count[i.lower()]-=1
                if count[i.lower()] < 0:
                    return False
            except:
                return False

    if all(i==0 for i in count.values()):
        return True
    else:
        return False

print(isAnagram('Hi babay', 'hi babay'))
