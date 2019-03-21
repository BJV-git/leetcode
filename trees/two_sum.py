# logic: better to maintain a seen instead of each for node and replicating

def findTarget(self, root, k):
    if not root: return False
    seen = set()

    def find(root):
        if not root: return
        if k - root.val in seen:
            return True
        else:
            seen.add(root.val)
        return find(root.left) or find(root.right)

    a = find(root)
    if a:
        return True
    else:
        return False
