# as given non empty we can just go ahead, normally no need of having the again recursive func written

# logic: go until we find same root value and run the check function
def isSubtree(s,t):
    self.val = 0
    if s == t:
        return True

    def check(a, b):  # lets just pass the reference as we know other , a be the main tree
        if not a and not b: return True
        if (not a and b) or (not b and a):
            return False
        # print(a.val,b.val)
        if a.val != b.val:
            return False
        return check(a.left, b.left) and check(a.right, b.right)

    def go(root):
        if root:
            if root.val == t.val:
                temp = t
                result = check(root, temp)
                if result == True:
                    self.val += 1

            go(root.left)
            go(root.right)

    go(s)

    return self.val > 0