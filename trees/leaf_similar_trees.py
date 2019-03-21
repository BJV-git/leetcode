# logic: lets do the inorder and see if both left and right are None
# not needed to check in same paths but end result

def leafSimilar(a,b):
    self.res1 = []
    self.res2 = []

    def inorder(root, arr):
        if root:
            inorder(root.left, arr)
            inorder(root.right, arr)
            if not root.left and not root.right:
                arr.append(root.val)

    inorder(a, self.res1)
    inorder(b, self.res2)

    return self.res1 == self.res2



