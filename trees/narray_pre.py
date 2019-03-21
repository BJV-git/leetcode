# just follow the normal way

def preorder(self, root):
    if not root: return []
    self. res =[]
    def trav(node):
        self.res.append(node.val)
        if node:
            for i in node.children:
                trav(i)

    trav(root)
    return self.res