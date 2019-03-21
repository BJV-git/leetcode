

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def unival(root):

    if not root: return False

    valu = root.val

    def check(node):
        if not node: return True
        if node.val != valu: return  False

        return check(node.left) and check(node.right)

    return check(root)