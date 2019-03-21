# logic: just can go in in order traversal and assign at root to the every right instead of print

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def increasingBST(self, root):
    if not root: return []
    global track
    main_node = TreeNode(None)
    track = main_node

    def inorder(node):
        if node:
            inorder(node.left)
            new = TreeNode(node.val)
            global track
            track.right = new
            track = track.right
            inorder(node.right)

    inorder(root)
    return (main_node.right)