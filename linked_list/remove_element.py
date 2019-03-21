


def remove(head, val):
    if not head: return head
    prev_node=None

    safe = head


    while head!=None:
        if head.val == val:
            temp = head
            while temp!=None and temp.val ==val:
                temp = temp.next

            if safe == head: # to check is the start has the repeated values
                safe = temp

            head = temp
            if prev_node:
                prev_node.next = temp


        prev_node = head
        if head:
            head = head.next


    return safe