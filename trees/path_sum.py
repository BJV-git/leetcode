# logic: from top to bottom pass the parents sum so that each get added, when ever we get the required sum, lets see if the node is leaf
# else return False - now may be another time we might have summ in different path so better retunr or of the truth values

# test cases learned: nee to be careful about what we are returning, best way is to make sure where my lines are gonna messup

def pathsum(root,summ):
    def hasPathSum(self, root, summ):

        if root:  # main
            total = summ
            ini = root.val

            # print(ini, 'ini')

            def find(root, ini):
                # print(ini)
                if root:  # in recursion to meet the edge cases
                    if root.val + ini == total and not root.left and not root.right:
                        return True

                    else:
                        return find(root.left, ini + root.val) or find(root.right,
                                                                       ini + root.val)  # no use the true or as end result will be
                        # true always
                else:
                    return False

            return find(root, 0)
        else:
            return False