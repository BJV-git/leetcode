# diversion from palindrome partition problem
# so we go through the each element and see if that can be a middle element of the longest palindrome

# palindrome can be either be from one element in middle, or , can be two elements and then teh same condition or, can be a continuous
# monotonous string

# we can also skip to middle as the elements before to that doesn't have the ones like the middle and don't have

def longestPalindrome(s):
    slen=len(s)
    max_pal=1
    max_pal_str=''

    limit  = slen
    if limit <2:
        return s
    if s==s[::-1]:
        return s

    i = 0

    while i < limit:
        slice_start = 0
        slice_end = 0

        print("i value and limit", i, limit)
        pres = s[i]
        j=i+1
        while j < slen and pres == s[j]:
            j+=1
        # lets calculate the distance
        diff = j-i
        print("for i {0} the diff is {1}".format(i,diff))
        # first to make sure if we can move as soon as possible, so checking if can

        if diff > 1: # we proceed only if the difference is > 1 else its just a single element

            count=0
            trace=start=end=0

            trace = i + ((diff-1) // 2)
            shift = trace+1

            if diff%2==1: # for odd length can find the middle

                count+=1
                start = trace -1
                end = trace+1
            else:
                count+=2
                start = trace -1
                end = trace + 2

            # print("")
            # print("start", start)
            # print("end", end)

            while start >=0 and end < slen and s[start]==s[end]:
                count +=2
                start-=1
                end+=1

            if count >= max_pal:


                max_pal = count
                print("here {0} {1}".format(start,end), s[start+1:end])
                max_pal_str=s[start+1:end]
                slice_start = start + 1
                slice_end = end
            # print("after entering the max_pal value is", max_pal)
            limit = slen - (max_pal // 2)

            # if max_pal%2 ==0:
            #     limit = slen - (max_pal//2) -1
            # else:
            #     print("slen", slen)
            #     limit = slen- (max_pal // 2) - 1
            print("limit set to", limit)
            #     print("")

            i = max(i+1, trace+1)
            i = shift
            # print("")
            # print("i", i)
            # print("limit" ,limit)

        else: # we chose to iterate normally
            start = i-1
            end = i+1

            count=1
            while start >=0 and end < slen and s[start]==s[end]:
                count +=2
                start -= 1
                end += 1

            if count >= max_pal:
                max_pal = count
                print("here {0} {1}".format(start,end),s[start+1:end] )
                max_pal_str = s[start +1:end]
                slice_start = start + 1
                slice_end = end
            limit = slen - (max_pal // 2)

            # if max_pal % 2 == 0:
            #
            #     limit = slen - (max_pal // 2) - 1
            # else:
            #     limit = slen - (max_pal // 2) - 1
            print("limit set to", limit)
            i+=1

    # print("max pal string ",max_pal_str)

    print("slice start is {0} and slice end is {1}".format(slice_start, slice_end))
    # print(s[0:slice_start]," and then " , s[slice_end:], "aha")

    return max_pal_str



#
# a='hi this is JB'
# alen = len(a)
# for i in range(alen):
#     print(a[i])

print(longestPalindrome("adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece"))
# print(len(longestPalindrome("adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece")))
print('abcabceee'[6:9])
# if 'abcabceee'[8:]:
#     print('hello')

