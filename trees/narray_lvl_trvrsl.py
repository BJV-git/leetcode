

def nara_lvl_trvrsl(root):
    if not root: return []
    queue=[root]
    self.res=[]
    while queue:
        self.res = [i.val for i in queue]
        queue = [child for node  in queue for child in node.children]
    return self.res