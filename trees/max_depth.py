


def maxDepth(tree):
    if tree:
        if tree.left and tree.right:
            return 1 + max(maxDepth(tree.left), maxDepth(tree.right))
        elif tree.left:
            return 1+ maxDepth(tree.left)
        else:
            return 1+ maxDepth(tree.right)

    else:
        return 0