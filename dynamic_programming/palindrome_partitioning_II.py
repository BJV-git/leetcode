# logic: we can find the largest possible palindrome in a given string, lets say that if not and can take only small part and leave the rest to
# others to minimize and can reduce the other cuts, then need to give away on both sides, so which means it increases the cuts on botjh sides, if
# were able to get on both sides then again they can be merged to main one

# so finding the best one in given string and doing recursively can give the solution i.e. finding the no of max palindromes

# can do it in o(n^2) as we pass every element we can check if that point can lead us to the best, else can move to next
# also we can cut the limit to which the max we found, let us say in midd.sle we found 5 as max means no need of going next to last but but one
# as even found no use. so if in middle we found greater automatically the limit would end the loop with out going further

# better to slice rather than split, as we might loose the necessary data if the repeated sequence is repeated else where
# abcabc or abcabceee


def minCut(s):

        arr=[]
        arr.append(s)
        cuts=0
        print("len is {0}".format(len(s)))

        while arr:
            s=arr[0]
            slen=len(s)
            slice_start=0
            slice_end = 0
            max_pal = 1
            max_pal_str = ''

            limit = len(s)
            if limit < 2 or s==s[::-1]:
                del arr[0]
                continue

            i = 0

            while i < limit:

                pres = s[i]
                j = i + 1
                while j < slen and pres == s[j]:
                    j += 1
                diff = j - i

                if diff > 1:  # we proceed only if the difference is > 1 else its just a single element

                    count = 0
                    trace = start = end = 0

                    trace = i + ((diff - 1) // 2)
                    shift = trace + 1

                    if diff % 2 == 1:  # for odd length can find the middle

                        count += 1
                        start = trace - 1
                        end = trace + 1
                    else:
                        count += 2
                        start = trace - 1
                        end = trace + 2

                    while start >= 0 and end < slen and s[start] == s[end]:
                        count += 2
                        start -= 1
                        end += 1

                    if count >= max_pal:
                        max_pal = count
                        max_pal_str = s[start + 1:end]
                        slice_start = start+1
                        slice_end = end
                    limit = slen - (max_pal // 2)


                    i = max(i + 1, trace + 1)
                    i = shift
                else:  # we chose to iterate normally
                    start = i - 1
                    end = i + 1

                    count = 1
                    while start >= 0 and end < slen and s[start] == s[end]:
                        count += 2
                        start -= 1
                        end += 1

                    if count >= max_pal:
                        max_pal = count
                        max_pal_str = s[start + 1:end]
                        slice_start = start + 1
                        slice_end = end
                    limit = slen - (max_pal // 2)

                    i += 1

            temp=[]
            temp.extend([s[0:slice_start],s[slice_end:] ])
            temp=[i for i in temp if i]
            cuts += len(temp)
            temp = [i for i in temp if len(i)>1]


            del arr[0]
            print("temp array", arr,'\n')

            # temp=[i for i in s.split(max_pal_str) if i]


            arr.extend(temp)


        return cuts

print(minCut("adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece"))

# a='sdsdfsvsfvsfvsfgasdadrefaef'
# a = a.split('g')
# print(a)
# del a[a.index('sdsdfsvsfvsfvsf')]
# print(a.split('fvsfgasdadrefaef'))