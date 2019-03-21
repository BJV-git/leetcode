# better to go with the while loop till found a new one
# BIG LEARNED: we need to be concurrent about using a head or head.next through out the program loop

def remove_dup(head):
    prev = None

    safe = head

    if not head or head.next == None:
        return head
    prev_node = None

    while head != None:

        if prev != head.val:
            prev = head.val
        else:
            # start while
            temp = head
            while temp != None and temp.val == prev:
                temp = temp.next
            prev_node.next = temp
            if temp:
                head = temp.next
                prev_node = temp
                prev = temp.val
            else:
                break

            continue

        prev_node = head
        head = head.next

    return safe