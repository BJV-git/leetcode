# logic: is as the best way to split for half and make it as a node , as a parent of the subtree and recursive
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sortedArrayToBST(nums):
    def sortedArrayToBST(self, nums):
        len_nums = len(nums)

        def convert(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = convert(left, mid - 1)
            node.right = convert(mid + 1, right)
            return node

        return convert(0, len_nums - 1)

