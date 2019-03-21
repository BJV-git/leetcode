# logic: rei, start from last and give the output

def len_last_word(s):
    count=0

    slen=len(s)
    for i in range(slen-1,-1,-1):
        if s[i].isalnum():
            count+=1
        elif count > 0:
            return count
        else:
            pass

    return count


print(len_last_word("a    "))