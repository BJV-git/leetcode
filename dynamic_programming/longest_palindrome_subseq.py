# logic: lets divide the given string into a combination of strings such that each is max possible palindrome
# now while combining we can eliminate the ones which contribute to the best

# or basically from one element can do either continuously check if equal and go on, or better is to just add when ever we happen to
# find the palindrome pattern

# a good way: can be to maintain two dictionaries left and right, so that we calculate the number of chars that have equal numbers
# means its enough we have those irrespective of the order -- NO: order matter for palindrome

# however it is useful to keep track of the left and right matching possibilities and then can pull all the chars order on one side,
# and can verify the order on other side and can break and add whenever not in sync

# maintain a dict for left and right, for all find the lcs as dicts, shouldn't take more than, o(n)

# the solution that can work seems like, see if can build as long sequence as possible, when met next not delete or replace but start new one
# caz not to loose the current longest from a point when met new one, also not deleting allows us to explore next best

# ex: 'arbjbuuab' 'babauu'



# *********************
# worked : its the same as above and will have to find the longest continuous increasing seq
# for above example: we get 1 2, 0 4 5 , 1 2 there fore longest is 12 45 which is answer

# another example: arbjbbab, babu
# 1 2, 0 2, 1 2  so 012 is the ans (# may b a better way to find out the longest is to have max and min first and then estimating the max possibility)
#

def longestPalindromeSubseq(s):

    left_dict = {i:[] for i in set(s)}
    right_dict = {i:[] for i in set(s)}
    slen = len(s)


    left_arr =""; left_len=0
    # right_len=slen;
    right_arr=s

    max_len=1

    limit=slen

    i=0

    while i < slen:
        right_dict[s[i]].append(i)
        i+=1

    i=0


    while i < limit:
        print(i)

        pres=s[i]

        left_arr += pres; left_len+=1; left_dict[pres].append(i)

        right_arr=right_arr[1:]
        # if right_dict[pres]:
        # print(i,pres, left_dict, '     ',right_dict)
        del right_dict[pres][0] # right_len -= 1;
        # need to find the LCS
        # print("after")
        # print(i, pres, right_dict)
        # print("")

        l = 0
        result = []
        temp = left_arr[::-1]
        right_k = [i for i, j in right_dict.items() if j]



        if i ==4:
            print("temp left, temp right","    ", left_dict,"and ", right_dict)
            print("left_len", left_len)
            print("right k", right_k)
            print("temp arr",temp)
            exit()

        while l < left_len:

            if temp[l] in right_k:

                if result and result[-1][1] > right_dict[temp[l]][0]:
                    right_dict[temp[l]].append(result[-1][1])
                    right_dict[temp[l]].sort()
                    del result[-1]

                result.append(  [  temp[l] , right_dict[temp[l]][0] ] )
                del right_dict[temp[l]][0]




            l += 1
        if i == 3:
            print(" result ", result)

        for a in result: # just update the right dict
            if a[1] > left_len:

                right_dict[a[0]].append(a[1])
                # print(right_dict[i[0]])
                right_dict[a[0]].sort()

        max_len = max(2*len(result),max_len)
        if result and temp[0]!=right_arr[0] :
            max_len+=1
        if i == 4:
            print("the max_len we got is ", max_len)
            exit()

        # adjust the limit

        limit = slen - (max_len//2)

        i+=1


    return max_len



print(longestPalindromeSubseq("jbrababu"))

a = 'arbjbab'; b='babu' # may be we can see if had a number that is greater than the current index i.e. max(i, max(right_dict[temp[l]]))
# as our goaL is to move to the left possible to grab as many as possible, we move by replacing as it makes the number of count same
# so when found a thing will see if had the same element next or not else its just the same......
# or can we get these in increasing order.????

# def longestPalindromeSubseq(s):
#
#     left_dict = {i:[] for i in set(s)}
#     right_dict = {i:[] for i in set(s)}
#     slen = len(s)
#
#
#     left_arr =""; left_len=0
#     # right_len=slen;
#     right_arr=s
#
#     max_len=1
#
#     limit=slen
#
#     i=0
#
#     while i < slen:
#         right_dict[s[i]].append(i)
#         i+=1
#
#     i=0
#
#
#     while i < limit:
#
#         pres=s[i]
#
#         left_arr += pres; left_len+=1; left_dict[pres].append(i)
#
#         right_arr=right_arr[1:]
#         # if right_dict[pres]:
#         print(i,pres, right_dict)
#         del right_dict[pres][0] # right_len -= 1;
#         # need to find the LCS
#         print("after")
#         print(i, pres, right_dict)
#         print("")
#
#         l = 0
#         result = []
#         temp = left_arr[::-1]
#         right_k = [i for i, j in right_dict.items() if j]
#
#         temp_left_dict = left_dict
#         temp_right_dict = right_dict
#
#         # if i ==4:
#         #     print("temp left, temp right","    ", temp_left_dict,"and ", temp_right_dict)
#         #     print("left_len", left_len)
#         #     print("right k", right_k)
#         #     print("temp arr",temp)
#         #     exit()
#
#         while l < left_len:
#
#             if temp[l] in right_k:
#
#
#                 if result and result[-1][1] > temp_right_dict[temp[l]][0]:
#                     temp_right_dict[temp[l]].append(result[-1][1]).sort()
#                     del result[-1]
#
#                 result.append(  [  temp[l] , temp_right_dict[temp[l]][0] ] )
#                 del temp_right_dict[temp[l]][0]
#
#                 if i == 1:
#                     print(right_k, ' ', temp[l], '  ',result)
#
#             l += 1
#
#         if i==1:
#             print("left_dict and right oriignal", left_dict,"   ", right_dict)
#             exit()
#
#         max_len = max(2*len(result),max_len)
#         if result and temp[0]!=right_arr[0] :
#             max_len+=1
#         if i == 4:
#             print("the max_len we got is ", max_len)
#             exit()
#
#         # adjust the limit
#
#         limit = slen - (max_len//2)
#         i+=1
#     return max_len
#
#
#
#
#
#
#
# print(longestPalindromeSubseq("jbrababu"))
#
#
#
#
