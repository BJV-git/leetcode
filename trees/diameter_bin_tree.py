# logic: just need to return the max i.e. height and max sum of the both left height adn right height

def diameterOfBinaryTree(root):
    if not root: return 0

    def height(root, maxi):
        if root:
            left_h = height(root.left, maxi)
            right_h = height(root.right, maxi)

            return [1 + max(left_h[0], right_h[0]), max(maxi, left_h[0] + right_h[0])]
        else:
            return [0,0]

    return height(root, 0)[1]

    # self.val = 0
    #
    # def height(root):
    #     if not root: return 0
    #     left_h = height(root.left)
    #     right_h = height(root.right)
    #     self.val = max(self.val, left_h + right_h)
    #
    #     return 1 + max(left_h, right_h)
    #
    # height(root)
    #
    # return self.val