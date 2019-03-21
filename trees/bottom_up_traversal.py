# logic: just traverse and append in first of stack, the right and then the left
# return the recursive lc + recursive rc .extend [l.val, r.val]

# learned: we can use queue inorder to keep track of the numbers we get at each stage and then append fo later
def levelOrderBottom(root):
    if not root: return []
    res,queue=[], [root]
    while queue:
        res.append([q.val for q in queue])
        queue = [child for node in queue for child in (node.left, node.right) if child]
    return list(reversed(res))
