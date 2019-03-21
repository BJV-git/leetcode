# can find all the paths and then see what are possible - again it would then be, dynamic prob

# from leaves can return the sum from bottom and from that node

# any ways we need to find the complexity at every node to check if we have the sum, so lets fo it all means
# even though the sum might get crossed may be next it might compensated

# so basically its a combination of the BFS and DFS
# can pass the sum from the top to the nodes and then, will increment total when ever the sum meets the sum

def pathSum(root, sum):
    res=[]

    def dfs(root, t):
        if root:
            if root.val + t == sum:
                global total
                total +=1
            dfs(root.left, t+root.val)
            dfs(root.right, t+root.val)

    if not root: return []
    queue=[root]
    while queue:
        _=[dfs(i,0) for i in queue]
        queue = [child for node in queue for child in (node.left, node.right) if child]
    return len(res)