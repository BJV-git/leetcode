# logic :: only need to go to right and stop at but one node
# better to store the parent value

# better going for the last but one and see if at all any smaller nodes exist
def second_min(root):
    if not root: return -1
    self.first = root.val
    self.stack = [sys.maxsize, sys.maxsize]
    self.encountered = 0

    def min(root):
        if not root: return

        if root.val != self.first:
            self.encountered = 1
        if root.val < self.stack[1] and root.val not in self.stack:
            self.stack[1] = root.val
            self.stack.sort()

        min(root.left)
        min(root.right)

    min(root)
    if self.encountered == 0:
        return -1
    else:
        return self.stack[1]






































    # mini=[0,0]
    #
    # def find(root):
    #     if not root:
    #         return
    #     if root.val > mini[0] and root.val not in mini:
    #         mini[0] = root.val
    #         mini.sort()
    #     find(root.right)
    # find(root)
    #
    # if mini[0]!=mini[1]:
    #     return mini[0]
    # else:
    #     return -1