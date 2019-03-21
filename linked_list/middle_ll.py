

def middle(head):
    if not head or head.next == None: return head

    l =0
    start = head
    while head!=None:
        l+=1
        head=head.next

    target = l//2

    while target >0:
        start = start.next
    return start