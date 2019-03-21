# logic: if we found a value that is greater than our r, we can eliminate all the right child as we dont need those values
# same goes with the left

def trimBST(root,l,r):
    if not root: return

    root.left = trimBST(root.left,l,r)
    root.right = trimBST(root.right, l, r)

    if l <= root.val <= r:
        return root
    if root.val < l:
        return root.right
    if root.val > r:
        return root.left