# as mentioned there are even numberred, not hiding, so we can find the solution just next to it
# can use the while loop

# learned from test case: not just about finding the unequal and it has to be the opposite one odd - even

def sort_iis_parity(A):

        odd=[]
        even =[]
        i=0
        while A:

            a = A.pop()
            if a%2==0:
                even.append(a)
            else:
                odd.append(a)
            i+=1
        for j in range(i//2):
            A.append(even.pop())
            A.append(odd.pop())
        return A



        # i=0
        # l = len(A)
        # while i < l:
        #     if i%2 != A[i]%2:
        #         print(i)
        #         temp=i+1
        #         while temp < l and A[temp]%2==i%2 and temp%2 == A[temp]%2:
        #             temp+=1
        #         print('foudn at ', temp)
        #         if temp < l:
        #             A[i], A[temp] = A[temp], A[i]
        #
        #     i+=1
        # return A

print(sort_iis_parity([648,831,560,986,192,424,997,829,897,843]))