# logic: just can return the min of both

# learned is that we need to go to the nearest leaf node, so need to traverse
# so we need to stop going to the null nodes by telling in the conditions

def minDepth(tree):
    if tree:
        if tree.left and tree.right:
            return 1 + min(minDepth(tree.left), minDepth(tree.right))
        elif tree.left:
            return 1+ minDepth(tree.left)
        else:
            return 1+ minDepth(tree.right)

    else:
        return 0