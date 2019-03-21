# logic: the max over lap is not gonna be more than the smaller of both. and same with the 0 or 1
# simple solution can be that run through all possibilities
# logic: after  getting the lists we can slide the smaller one over the top and see how many identical array elements we get
# repeated while subtracting means that there is a pattern and we take the max of it. (if met the max_possbl return)

# working if the order is as it is, missing when in between some other are coming, the common pattern is missing
# better to chase if we can reach max by sliding it more than max value till calculated and with in possibility

# missing if the pattern is not captured correctly
# better to convert all into list and then slide

def largestOverlap(A, B):
    rows = cols = len(A)
    # lista = [[i,j] for i in range(rows) for j in range(cols) if A[i][j]==1 ]
    # listb = [[i,j] for i in range(rows) for j in range(cols) if B[i][j] == 1]

    lista = [[i, j, A[i][j] ] for i in range(rows) for j in range(cols)]
    listb = [[i, j, B[i][j]] for i in range(rows) for j in range(cols)]

    total = rows*cols

    # len_a = sum([1 for ])
    # len_b = len(listb)
    max_overlap=0

    print(lista, "list a")
    print(listb, "list b")

    patterns1 = [[(lista[j + i][0] - listb[j][0], lista[j + i][1] - listb[j][1]) for j in range(total) if j + i < total and lista[j+i][2]==1 and listb[j][2]==1] for i in range(total)]
    patterns2 = [[(listb[j + i][0] - lista[j][0], listb[j + i][1] - lista[j][1]) for j in range(total) if j + i < total and listb[j+i][2]==1 and lista[j][2]==1] for i in range(total)]
    print("patterns1", patterns1)
    print("patterns2", patterns2)
    counts1 = [p.count(e) for p in patterns1 for e in set(p)]
    if counts1==[]:
        max_overlap1= 0
    else:
        max_overlap1 = max(counts1)
    counts2 = [p.count(e) for p in patterns2 for e in set(p)]

    print("count1", counts1)
    print("count2", counts2)
    if counts2==[]:
        max_overlap2= 0
    else:
        max_overlap2 = max(counts2)
    # print(max_overlap)
    return max(max_overlap1, max_overlap2)

    # max_possible_overlap = min(len_a, len_b)
    # if max_possible_overlap ==1 and len_a > 0 and len_b > 0:
    #     return 1
    # elif max_possible_overlap==0:
    #     return 0
    # elif len([ list(x) for x in set(map(tuple, lista)).intersection(map(tuple,listb)) ]) == max_possible_overlap:
    #     return max_possible_overlap
    # else:
    #     if len_b > len_a:
    #         listb, lista = lista, listb
    #         len_a, len_b = len_b, len_a
    #     patterns = [[(lista[j + i][0] - listb[j][0], lista[j + i][1] - listb[j][1]) for j in range(len_b) if j+i < len_a] for i in range(len_a) ]
    #     print("pattern", patterns)
    #     max_overlap =  max([p.count(e) for p in patterns for e in set(p)])
    #     # print('pattern',patterns)
    #     # print("max_overlap", max_overlap)
    #     # exit()
    #     return max_overlap
        #
        # if len_a > len_b:
        #     diff = len_a - len_b +1
        #     for i in range(diff):
        #         patterns = [ (lista[j+i][0] - listb[j][0] , lista[j+i][1] - listb[j][1]) for j in range(len_b)  ]
        #         print("patterns {0}".format(i), patterns)
        #         pattern = max(set(patterns), key=patterns.count)
        #
        #         max_overlap = max(max_overlap,max([patterns.count(e) for e in set(patterns)]) )
        #     return max_overlap
        #
        # elif len_b > len_a:
        #     diff = len_b - len_a + 1
        #     for i in range(diff):
        #         patterns = [(listb[j + i][0] - lista[j][0], listb[j + i][1] - lista[j][1]) for j in range(len_a)]
        #         print("patterns {0}".format(i), patterns)
        #         max_overlap = max(max_overlap, max([patterns.count(e) for e in set(patterns)]))
        #     return max_overlap
        #
        # else:
        #     patterns = [(listb[j ][0] - lista[j][0], listb[j ][1] - lista[j][1]) for j in range(len_a)]
        #     return max(max_overlap, max([patterns.count(e) for e in set(patterns)]))



print(largestOverlap([[1,0],[0,0]],[[0,1],[1,0]]))

# a=[[0, 0], [0, 1], [1, 1], [2, 1]]
# b= [[1, 1], [1, 2], [2, 2]]
#
# diff = len(a) - len(b) +1
# i=0
# patterns = [ (a[j+i][0] - b[j][0] , a[j+i][1] - b[j][1]) for j in range(len(b))  ]
# print(max([patterns.count(i) for i in set(patterns)]))
# i=1
# patterns = [ (a[j+i][0] - b[j][0] , a[j+i][1] - b[j][1]) for j in range(len(b))  ]
# print(max([patterns.count(i) for i in set(patterns)]))