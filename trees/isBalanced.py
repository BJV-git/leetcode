# logic: return the difference of heights as <=1 condition

# as we either need ot find the height or flase at oen time, lets return the both i.e. height adn the truth value

def isBalanced(root):
    def isBalanced(self, root):

        def get(root):
            if root and (root.left or root.right):
                # print(root.val)
                left = get(root.left)
                right = get(root.right)
                # print(left)
                # print(right)
                # print(' ')

                return (1 + max(left[0], right[0]),
                        (left[1] and right[1]) and (max(left[0], right[0]) - min(left[0], right[0]) <= 1))
            elif root:
                return (1, True)

            else:
                return (0, True)

        return get(root)[1]