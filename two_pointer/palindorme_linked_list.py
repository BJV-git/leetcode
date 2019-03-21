# logic: go to half and reverse the list and then track from both ends

def palin_ll(head):
    if not head or head.next == None:
        return True
    l = 1
    temp = head
    while temp.next != None:
        temp = temp.next
        l += 1
    right_start = 0
    if l % 2 == 0:
        right_start = l // 2
    else:
        right_start = l // 2 + 1

    # go to half and reverse

    def reverse_ll(head):

        prev = None
        curr = head

        while curr != None:
            next = curr.next

            curr.next = prev
            prev = curr
            curr = next

        return prev

    start = right_start
    temp = head
    prev = None

    while start > 0:
        prev = temp
        temp = temp.next
        start -= 1
    prev.next = None

    temp = reverse_ll(temp)

    # to avoid the limits we go till the right end equals

    while temp != None:
        if head.val != temp.val:
            return False
        head = head.next
        temp = temp.next
    return True