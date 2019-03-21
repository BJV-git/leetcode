# logic: just need to  print all root to leaf paths
# similar to the finding the number of leaf nodes,

# sol 1: we can pass the till time encountered parent nodes # will occupy extra lot of space and redundancy
# but either ways we gonna have to use that space

# sol 2: we can use DFS

def binaryTreePaths(root):
    res=[]

    def paths(root,prev):
        if not root:
            return
        elif not root.left and not root.right:
            res.append(prev + str(root.val))
        else:
            paths(root.left, prev+str(root.val)+ '->')
            paths(root.right, prev+str(root.val) + '->')

    paths(root,'')
    return res