# can maintain the highest mode at each node as it is bst, if equal will append all we need to do is just
# track to left how much same numbers are there


# key observation: can while loop at every node for finding similar values to get the mode, using the arch for max,
# if next lets ignore if node.val == already mode

# important learned (from mode updating) is nto advisable to change with just an assignment but better toi update




# from bst if we do in-order traversal, we get the numbers in increasing manner, so that we can get numbers in order to decide


def findMode(self, root):
    if not root: return []
    def inorder(root):
        if root:
            yield from inorder(root.left)
            yield root.val
            yield from inorder(root.right)

    # now as the numbers are in order, to get
    mode = []
    curr_max = 0
    count=-1
    curr_v=None

    for i in inorder(root):
        if i != curr_v: # encountered a new one
                if count> curr_max: # new mode
                    mode=[curr_v]
                    curr_max=count
                elif count == curr_max:
                    mode.append(curr_v)
                curr_v =i
                count=1
        else:
            count+=1


    if count > curr_max:  # new mode
        mode = [curr_v]
    elif count == curr_max:
        mode.append(curr_v)
    print(mode)
































    # mode = [[None, 0]]
    #
    # def find(root):
    #     if root:  # finding the new
    #         if root.val != mode[0][0]:  # only if the mode is not equal we try to give it a shot and see if fits
    #             maxi = root.val
    #             left_temp = root.left
    #             right_temp = root.right
    #             count = 1
    #             while left_temp or right_temp:
    #                 if left_temp and left_temp.val == mode[0][0]:
    #                     count += 1
    #                     left_temp = left_temp.left
    #                 if right_temp and right_temp.val == mode[0][0]:
    #                     count += 1
    #                     right_temp = right_temp.right
    #                 if right_temp.val != mode[0][0] and left_temp != mode[0][0]:
    #                     break
    #             # exchange if possible
    #
    #             if mode[0][1] < count:  # fresh the mode
    #                 global  mode
    #                 mode = [[None, 0]]
    #                 mode[0][0] = maxi
    #                 mode[0][1] = count
    #             elif mode[0][1] == count:
    #                 mode.append([root.val, count])
    #             find(root.left)
    #             find(root.right)
    #
    # find(root)
    # print(mode)