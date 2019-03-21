# paths always deal with the dfs, so lets do recursive stuff

# as it is path, we need to see from each node till what extennt on both sides we cna go
# plain is to go with BFS adn at each need to check as we are not usre where it miht get repeated second time,

# effecient way is to visit nodes

# for paths, when evr we encounter, a leaf or a not == same value or some condition node it means that is a path
# lets solve it as the diameter one, i.e. choosing the best among left and right which has the max chain, and we proceed only if we have
# equal root value

def LUP(root):
    if not root: return 0

    self.curr = root.val
    self.count=0
    self.maxi=0

    def l(root, c):
        if not root:
            return 0
        if root.val != c:
            return 0
        return 1+ max(l(root.right),l(root.left))

    queue=[root]
    while queue:
        self.maxi = [max(self.maxi, l(i,i.val)) for i in queue][-1]
        # for i in queue:
        #     l(i, i.val)
        #     self.maxi = max(self.maxi, self.count)
        #     self.count = 0
        queue = [child for node in queue for child in (node.left, node.right) if child]
    print(self.maxi-1)
