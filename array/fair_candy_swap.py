# logic: obviously oen sum is gonna be greater than another, can think as usually they used to be equal but been seperated back.
# as they are equal, we knew that after exchange they gonna be at  avg of sum1 and sum2
# so need to find the avg and then element required for that and give back the extra after sum

# normal pattern is that exchanging the max of both gives results to some extent - if so logic? =

# can take the smallest one. sort both. take from right of other and replace here in smaller from right, see whenever the summ meets,
# if goes less stop. so at same time we know what number to take and swap

# reason in choosing small is that we can do less iterations

# also distance from meet to individual sums can be considered to maximize the time reaching eff in sum
# here as there are equi distant nothing changes drastically4

# got accepted when removed the sort thing as taking extra time (need to do in facebook too)

def fairCandySwap(A, B):
    suma = sum(A)
    sumb = sum(B)
    lena = len(A)
    lenb = len(B)
    meet = (suma+sumb)//2
    flag = 0

    # A.sort()
    # B.sort()

    if sumb> suma:
        A, B = B,A
        suma, sumb = sumb, suma
        lena, lenb = lenb, lena
        flag=1
    print(A)
    print(B)

    for b in range(lenb-1, -1,-1):
        for a in range(lena-1, -1, -1):

            new_sum = sumb - B[b] + A[a]
            if new_sum == meet:
                if flag==0:
                    return [A[a], B[b]]
                else:
                    return [B[b], A[a]]

            if new_sum > 1.5*meet:
                print("A", A[a])
                print("B", B[b])
                break

print(fairCandySwap([35,17,4,24,10],[63,21]))