# logic:to reach every path, then try to get the left leaves appended to a res=[]

# to verify the things need to implement at the sub tree level

def sumOfLeftLeaves(self, root):
    if not root:
        return 0
    res = []

    def summ(root):
        if root:
            if root.left and not root.left.left and not root.left.right:
                res.append(root.left.val)
            summ(root.left)
            summ(root.right)

    summ(root)
    # print(res)
    return sum(res)
