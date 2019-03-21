# logic : if the input is given in array format then can solve it using iterations
# if need to solve in recursive manner


# learned: when need to see things at, height level, need ot use the BFS, like seeing if it is symmetric or level order traversal

# as we see in the inner for loop, we only have two things, so can repeat in recursive, i.e. we can check is each tree is symmetric or
# not as do it recursively

# as a matter of fact, this is the best way we can access the binary tree, as the tree splits two we also do split the recursion by two

def isSymmetric(self, root):
    if not root: return True
    res, queue = [], [root]
    while queue:
        res = [q.val if q else 0 for q in queue] # even though the value is null we want to make sure the value 0 is there to judge
        queue = [i for i in queue if i]
        if res != res[::-1]:
            return False
        queue = [child for node in queue for child in (node.left, node.right)]
    return True

    # def mirror(self, a, b):
    #     if not a or not b:
    #         return not a and not b
    #     return a.val == b.val and self.mirror(a.left, b.right) and self.mirror(a.right, b.left)
    #
    # def isSymmetric(self, root):
    #     return True if not root else self.mirror(root.left, root.right)