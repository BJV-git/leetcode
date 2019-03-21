# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        s = []

        def preorder(t):
            if t:
                s.append(str(t.val))
                if t.left and t.right:
                    s.append("(")
                    preorder(t.left)
                    s.append(")(")
                    preorder(t.right)
                    s.append(")")
                elif t.left:
                    s.append("(")
                    preorder(t.left)
                    s.append(")")
                elif t.right:
                    s.append("()(")
                    preorder(t.right)
                    s.append(")")
                else:
                    pass

        preorder(t)
        return (''.join(s))