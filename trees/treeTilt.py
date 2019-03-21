# logic: just return the sums, mean while in self update the value

def treetilt(root):
    def findTilt(self, root):
        self.total = 0

        if not root: return 0

        def getsum(root):
            if not root: return 0
            lsum = getsum(root.left)
            rsum = getsum(root.right)
            self.total += abs(lsum - rsum)
            # print('at root value', root.val, 'the diff is ', abs(lsum-rsum))
            return root.val + lsum + rsum

        getsum(root)
        return self.total