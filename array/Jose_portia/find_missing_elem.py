# logic: just we can count using the dict and can get the one with 1 count value the key and return
# as in the given condition said that they are same

# learned: best is to sum and then return diffrene of abs

def missing_elem(a,b):
    count={}
    for i in a:
        count[i] = count.get(i,0)+1
    for j in b:
        count[j]-=1
    for i,j in count.items():
        if j==1:
            return ((i,j))