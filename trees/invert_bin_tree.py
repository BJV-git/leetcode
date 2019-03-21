# logic: just at every node exchange the node references

def invertTree(self, root):
    if root:
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root