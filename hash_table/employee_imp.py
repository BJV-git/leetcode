# just can do the depth first search

def employees_imp(employees,id):
    d={}
    for i in employees:
       d[i.id] = [i.importance, i.subordinates]
    d={x[0]:[x[1],x[2]] for x in employees}
    print(d)

    count=0

    dfs=[id]
    while dfs:
        for i in dfs:
            count+=d[i][0]
        temployees=[]

        for sub in dfs:
            temployees.extend(d[sub][1])
        dfs=temployees
    return count

print(employees_imp([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1))