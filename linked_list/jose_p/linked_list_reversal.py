class Node(object):

    def __init__(self, value):
        self.value = value
        self.next=None

# logic: get the prev and curr nad then go on storing the temp
# i learned: if taken enough no of args then can work for all the cases

def reverse_ll(head):
    prev = None
    curr = head

    while curr != None:
        next = curr.next # like normal operation as we shift the next but we save it before
        curr.next = prev # set it
        prev = curr # shift
        curr = next

    return prev