# logic: dfs so just use it

def avg_levels(root):
    if not root: return []
    res=[]
    queue=[root]
    while queue:
        temp = [i.val for i in queue]
        res.append(float(sum(temp))/float(len(temp)))
        queue = [child for i in queue for child in (i.left, i.right) if child]
    return res