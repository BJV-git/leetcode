# learned: simply skip the duplicate node
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def remove_duplicate(head):
    if not head: return None
    found = 0
    zero = ListNode(-2)
    zero.next = head
    cur = zero
    prev = None
    while cur:  # for move on
        while cur.next and cur.next.val == cur.val:
            cur.next = cur.next.next
            found = 1
        if found != 1:
            prev = cur
        cur = cur.next
        if found == 1:
            prev.next = cur
            found = 0
            continue
    return zero.next