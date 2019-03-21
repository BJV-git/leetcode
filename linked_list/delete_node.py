# when given access to that node only
# so will just push the value and at last pop out
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def delete(node):

    while node.next!=None:
        curr = node.val
        next = node.next.val
        node.next.val = curr
        node.val = next
        node = node.next