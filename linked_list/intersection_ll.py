# logic: skip is internally may be he writes to evaluate the program

# better to push the data as from one point the data are equal, from the instance they are equal

# same logic as the linked list loop

def intersection(headA, headB):
    p, q = headA, headB;
    while p != q:
        p = p.next if p else headB;
        q = q.next if q else headA;
    return p;