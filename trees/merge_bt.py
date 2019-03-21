# logic: just add the nodes else the values

def mergeTrees(x,y):
    if not y:
        return x
    if not x:
        return y

    def merge(a, b):
        if not a and not b:
            return
        if a and b:  # if the other dont exist then no point in assigning left and rights
            a.val += b.val
        if b.left:
            if a.left:
                merge(a.left, b.left)

            else:
                a.left = b.left
        if b.right:
            if a.right:
                merge(a.right, b.right)
            else:
                a.right = b.right

    merge(x, y)
    return x

