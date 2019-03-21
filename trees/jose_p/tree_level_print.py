# logic: (brute) assign the numbers i.e. level score for each level of the items
# later in dict can sort and then print the things

# learned is breadth first search: using a queue and pushing parent elements in and popping children out
from collections import defaultdict


def level_print(root):
    l=0
    dic = defaultdict(list)
    def level_p(root,l):
        if root:
            dic[l].append(root.val)
            level_p(root.left, l+1)
            level_p(root.right, l+1)

    level_p(root,0)
    for i in range(len(dic)):
        print(dic[i])
        print("")

