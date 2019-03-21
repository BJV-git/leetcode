# logic : human logic - have count and track of numbers until reach new one if count >-3 append result
# learned: when deciding some things, need to make sure if they cover the edge cases.
# else: need to cover those edge cases

def largeGroupPositions(S):
    len_s = len(S)

    if  len_s < 3:
        return []
    else:
        curr_pos=0
        curr_char=S[0]
        curr_count = 1
        flag=0
        result=[]

        for i in range(1,len_s):
            if S[i] == curr_char:
                curr_count+=1

            if S[i] != curr_char or i == len_s-1:
                if curr_count >=3:
                    if i==len_s-1 and S[i] == curr_char:
                        result.append([curr_pos, i])
                        print("appending the results", result)

                    else:

                        result.append([curr_pos, i - 1])


                # else:

                curr_pos=i
                curr_count=1
                curr_char=S[i]
            print("index position", i)
            print("start_pos", curr_pos)
            print("ciurr_char", curr_char)
            print("curr_count", curr_count)
            print("")
        return result

print(largeGroupPositions("aaa"))
