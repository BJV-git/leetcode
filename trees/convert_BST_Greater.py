# logic: just in the inorder traversal exchange the left adn right

def convertBST(root):
    def convertBST(self, root):
        if not root: return []
        self.total = 0
        res = []

        def inorder(root):
            if root:
                inorder(root.right)
                root.val = root.val + self.total
                res.append(root.val)
                self.total = root.val
                inorder(root.left)

        inorder(root)
        return root