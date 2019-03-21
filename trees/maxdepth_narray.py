# logic: retunr 1 when it has node childs i.e. saying we met the parent having no child

def maxDepth(root):
    if not root: return 0
    if root.children:
        return 1 + max([self.maxDepth(i) for i in root.children])
    else:
        return 1
