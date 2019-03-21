

def searchBST(root,k):
    if root:
        if root.val == k:
            return root
        elif root.val > k:
            return searchBST(root.left, k)
        elif root.val < k:
            return searchBST(root.right,k)
    else:
        return None