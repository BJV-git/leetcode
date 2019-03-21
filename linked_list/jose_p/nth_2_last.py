class Node(object):

    def __init__(self, value):
        self.value = value
        self.next=None

# logic: assume the current node as the nth from last, maintain the count, when count is zero, the stored also moves to next for each
# iteration
# Instead of finding the length


def nth_2_last(head,n):
    node = head
    while head.next != None:

        if n <= 0:
            node = node.next
        head = head.next
        n-=1


    return node