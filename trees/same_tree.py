# logic: starting from test case, need to include try init so that, might nor fail

def isSameTree(self, p, q):
    if not p and not q:
        return True
    c = ((p and q) or (not p and not q))
    # print(c)
    if c:
        if p and q:
            if p.val != q.val:
                return False
            # print(p.val)
            # print(q.val)
            # print('')
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    if not c:
        return False