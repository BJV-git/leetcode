# logic: main is the flow and then temp_left and temp_right keep saving things
# also can do as take the start and end points of needed value and merge to the l1

def merge(l1, l2):
    # if a and b:
    #
    #     if a.val > b.val:
    #         a, b = b, a
    #     a.next = self.mergeTwoLists(a.next, b)
    # return a or b
    if not l1:
        return l2
    if not l2:
        return l1

        # taking first list as ref
    if l2.val < l1.val:
        l1, l2 = l2, l1
    start = l1
    end = l2

    main = l1

    while main and main.next != None:

        prev = main.val
        while main.next.next and main.next.val == prev:
            main = main.next

        if l2 and l2.val == prev:
            future_l1 = main.next
            main.next = l2

            while l2.next and l2.next.val == prev:
                l2 = l2.next
            future_l2 = l2

            l2 = l2.next

            future_l2.next = future_l1
            main = future_l2
            continue

        elif l2 and main.next and main.next.val > l2.val:

            future_l1 = main.next
            main.next = l2
            while l2.next and l2.next.val < main.next.val:
                l2 = l2.next
            future_l2 = l2

            l2 = l2.next


            future_l2.next = future_l1
            main = future_l2
            continue
        else:
            main = main.next
    if l2 != None and main:
        main.next = l2

    return start