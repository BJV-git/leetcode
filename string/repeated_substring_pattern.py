# logic: basically the limit of checking doesn't exceed the mid of the stuff, also if odd then has ro be single,
# and we check if can find the pattern by pushing the reference points

# obvious we need to find the pattern start point as the s[0]

# learned logic: so when removed the first and the last, means we are trying to see if there is atleast one sub division
# as we removed we have already removed two repetitions

def ifcanform(s):

    return (s + s)[1:-1].find(s) != -1

    # s = s.replace(' ', '')
    # slen = len(s)
    #
    # if slen == 1:
    #     return False
    #
    # if slen % 2 == 1 and len(set(s)) == 1:  # odd case
    #     return True
    # ref_e = 0
    #
    # i = 1
    #
    # while i < slen and s[i] != s[0]:
    #     i += 1
    #
    # if i > slen // 2:
    #     return False
    #
    # ref_e = i - 1  # first reference point
    #
    # i = ref_e + 1
    #
    # while i < slen:
    #     j = 0
    #     while j <= ref_e:
    #         try:
    #             if s[i] != s[j]:  # find the next end whose next is s[0]
    #                 i += 1
    #                 if i > slen // 2:
    #                     return False
    #
    #                 while i <= slen // 2:
    #                     if s[i] == s[0]:
    #                         print("new i is",i)
    #                         ref_e = i - 1
    #                         break
    #                     i += 1
    #                 break
    #             i += 1
    #             j += 1
    #         except:
    #             return False
    #
    # if ref_e > slen // 2 or s[-1] != s[ref_e]:
    #     return False
    # else:
    #     return True

print(ifcanform("abacababacab"))
# print(set('aaa'))