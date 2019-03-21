def postorder(self, root):
    if not root: return []
    self.res = []

    def trav(node):

        if node:
            for i in node.children:
                trav(i)
            self.res.append(node.val)

    trav(root)
    return self.res