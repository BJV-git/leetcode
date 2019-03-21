



def reverse_ll(head):
    if not head or head.next == None or head.next.next == None:
        return False
    slow = head
    fast = head.next

    while slow.next != None:
        if slow == fast:
            return True
        try:
            slow = slow.next
            fast = fast.next.next

        except:
            return False