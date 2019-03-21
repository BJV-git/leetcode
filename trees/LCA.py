# logic: to return the parent, if equal return or return that node parent

# observation: given a node can be its own descendant
# learned: if the tree is BST why not use it for advantage

# if we have a node in between the values of p and q, now lets return, also when one value is equal

def lowestCommonAncestor(root,p,q):
    if root.val > max(p.val, q.val):
        return lowestCommonAncestor(root.left, p, q)
    elif root.val < min(p.val, q.val):
        return lowestCommonAncestor(root.right, p, q)
    return root






























#     if None in (root, p, q):
#         return None
#     if root == p or root == q:
#         return root.val
#     if p==q:
#         return p.val
#     found=0 # can be used to stop other iterations - # looks like not possible
#
#     def find(root):
#         if root:
#             left = find(root.left)
#             right = find(root.right)
#             if left[1]==1: # see if its already solved
#                 return left
#             elif right[1]==1:
#                 return right
#             # if not then see if at that particiular node solved?
#
#             if (not left[0] and not right[0]): # means exactly at that point the two parents (of childs found) met
#                 return (root,1)
#             if root in (p,q) and (root.left in (p,q) or root.right in (p,q)): # found that sub tree itself
#                 return (root,1)
#
#             if (not left[0] or not right[0]) and root in (p,q): # same side but nor direct relation
#                 return (root,1)
#             if (root.left in (p,q) and root.right in (p,q)): # found the right parent which has children on both sides
#                 return (root,1)
#             if root.left in (p,q) or root.right in (p,q):
#                 return (root,0)
#             return (None,0)
#
#             # check if we have one among left and right so that we don't need to proceed
#         else:
#             return (None,0)
#     return find(root)[0]
#
# print(not None)