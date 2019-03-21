# logic: can recursively see if we had the property satisfied or not at each node level and then recursively
# if we can write the and logic at any time if it is False the entire is gonna be false and no need of checking all the things

# learned logic is if we do in order traversal the elems should be in sorted order
def bin_tree_check(root):

    if root: # taking care of the base case
        # the cases say that the root or the given tree falls under teh below catogery so either of those are capalbel of returning teh
        # answer. thats the same case carried with the rest too
        if root.left and root.right:
            if root.left.val <= root.val and root.val < root.right.val:
                return bin_tree_check(root.left) and bin_tree_check(root.right)
            else:
                return False
        elif root.left:
            if root.val >= root.left.val:
                return bin_tree_check(root.left)
            else:
                return False

        elif root.right:
            if root.val < root.right.val:
                return bin_tree_check(root.right)

        else:
            return True

    return False
