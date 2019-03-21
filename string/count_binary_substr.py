# logic: the counting starts at 01 or 10

def count_binary_packed(s):
    slen=len(s)
    count=0
    if slen < 2:
        return 0

    i=0

    while i < slen-1:
        if (s[i] == '0' and s[i+1]=='1') or (s[i] == '1' and s[i+1]=='0'):
            count+=1
            start = i-1
            end = i+2

            if s[i]=='0':
                left, right = '0','1'
            else:
                left, right = '1','0'

            while start>=0 and end < slen:
                if not(s[start]==left and s[end]==right):
                    i = end-2
                    break
                count += 1
                start-=1
                end+=1


        i+=1

    return count

print(count_binary_packed('11111110'))