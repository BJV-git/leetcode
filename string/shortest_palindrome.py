# logic: copy paste

# learned from test case: need to write so that if its first and we have extra same repeated to next need to minimize
# logic can work is that need to find out the possible palindrome from staring point, if so, then add remaining

# workable: find the largest palindrome from starting point and add the rest to it....
# so need to modify existing stuff so that, its stores the best first started palindrome

# while searching the only thing we need to move is right, and it would move with 2 speed as if one is not equal then would
# move by twice, and can track from there, also better to count continuous things too


# LEARNED: when need to analyze look for the min enough needed info for getting the result

def shortest_palindrome(s):

    slen = len(s)
    max_pal = 1
    max_pal_str = ''

    limit = (slen-1)//2

    if slen ==1 or s == s[::-1]:
        return s

    max_pal_str = s[0]


    # first lets find the continuous thing, that can make us move fast

    main_end=0

    cont=0

    while cont < slen:
        if s[cont] != max_pal_str:
            break
        cont+=1

    i = cont
    # print("cont", cont)
    main_end =  cont-1

    even_end=0
    odd_end=0
    odd_start=0
    even_start = 0


    while i <= limit and even_start<=slen//2 and odd_start <= slen//2 and (odd_end < slen or even_end < slen):

        # at every point I need to check if it can be an even or odd palindrome (from first)

        # cont is the index we get of the common element palindrome
        # at every stage need to check

        # check even palindrome ---------------------------------

        temp_start = max(i,odd_end)
        temp_end = temp_start + 1
        if i+1 < slen and s[i] == s[i+1]:
            while temp_start >= 0 and temp_end < slen and s[temp_start] == s[temp_end]:
                temp_start-=1
                temp_end+=1

            if temp_start ==-1: # means touched the start point
                even_end = temp_end-1
                even_start = max(i,odd_end)
        # print("i when entered",i)
        # print("after even check" ,even_end)
        # exit()


        #check the odd palindrome ---------------------------------
        # this limits of add will be changed to end and next as any intermediate found will be lesser than even

        temp_odd_start= max(i, even_end+1)
        temp_odd_end= 2*temp_odd_start

        z=0


        if temp_odd_end < slen and s[temp_odd_end] == s[0]: # the ends matched so can go ahead and search for odd palindrome
            while z < temp_odd_start and temp_odd_end > z and s[z]==s[temp_odd_end]:
                z+=1
                temp_odd_end-=1

            if z == temp_odd_start: # means reached the end saying that all are matched
                odd_end = 2*temp_odd_start
                odd_start = max(i, even_end+1)

        i+=1
    main_end = max(max(even_end, odd_end), main_end)
    return s[main_end+1:][::-1]  + s

print(shortest_palindrome('abbacd'))
# print('aaaaaaabaaaaaaacd'[14+1:])


    #
    #
    #
    #
    #
    # if cont
    # i = 0
    #
    # while i < limit:
    #     pres = s[i]
    #     j = i + 1
    #     while j < slen and pres == s[j]:
    #         j += 1
    #     diff = j - i
    #
    #     if diff > 1:
    #
    #         count = 0
    #         trace = start = end = 0
    #
    #         trace = i + ((diff - 1) // 2)
    #         shift = trace + 1
    #
    #         if diff % 2 == 1:
    #
    #             count += 1
    #             start = trace - 1
    #             end = trace + 1
    #         else:
    #             count += 2
    #             start = trace - 1
    #             end = trace + 2
    #
    #         while start >= 0 and end < slen and s[start] == s[end]:
    #             count += 2
    #             start -= 1
    #             end += 1
    #
    #         if count >= max_pal:
    #             max_pal = count
    #             max_pal_str = s[start + 1:end]
    #         if max_pal % 2 == 0:
    #
    #             limit = slen - (max_pal // 2)
    #         else:
    #             limit = slen - (max_pal // 2)
    #
    #         i = max(i + 1, trace + 1)
    #         i = shift
    #
    #     else:
    #         start = i - 1
    #         end = i + 1
    #
    #         count = 1
    #         while start >= 0 and end < slen and s[start] == s[end]:
    #             count += 2
    #             start -= 1
    #             end += 1
    #
    #         if count > max_pal:
    #             max_pal = count
    #             max_pal_str = s[start + 1:end]
    #
    #         if max_pal % 2 == 0:
    #
    #             limit = slen - (max_pal // 2)
    #         else:
    #             limit = slen - (max_pal // 2)
    #         i += 1
    # final = s.split(max_pal_str)
    # flen= len(final)
    # # print(final)
    # # print(max_pal_str)
    # if not final[0] and flen==2:
    #     remain = s.split(max_pal_str)[1]
    #     return remain[::-1] + max_pal_str + remain
    # else: # i.e. when not found starting string itself is a palindrome but only from middle
    #     # need to find the palindrome with start as mid
    #
    #     p = 0
    #     for i in range(1,slen):
    #         if not s[:i] == s[:i][::-1]:
    #             print(s[:i], "here is the ", i)
    #             p=max(0,i-1)
    #             break
    #     return s[p:][::-1] + s
    #     # if p%2==0:
    #     #     return s[p:][::-1]+s[((p-1)//2)+1:]
    #     #
    #     # else:
    #     #     p=(p)//2
    #     #
    #     #     return s[p+1:][::-1]+s[p:]
    #
