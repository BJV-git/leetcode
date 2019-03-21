# learned Logic:

# trimming

def trim_bst(tree, min, max):
    if not tree:
        return

    tree.left = trim_bst(tree.left, min, max)
    tree.right = trim_bst(tree.right, min, max)

    if min <= tree.val <= max:
        return tree
    if tree.val < min: # makes sense as we do not need those values any more
        return tree.right

    if tree.val > max:
        return tree.left
