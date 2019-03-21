# logic: rather checking at each level, can simply check teh middle ones

# learned: we can just compare from the point, where the unnecessary is to be avoided
import time

x = time.time()
def del_1_palindorme(s):
    slen=len(s)

    i=0
    j=slen-1

    while i<j:
        if s[i]==s[j]:
            i+=1
            j-=1
        else:
            break
    if i>=j:
        return True
    return s[i+1:j+1]==s[i+1:j+1][::-1] or  s[i:j]==s[i:j][::-1] # to consider the jth element also and on to the other hand also


print(del_1_palindorme("deeee"))
print(time.time() - x)