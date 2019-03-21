class Node(object):

    def __init__(self, value):
        self.value = value
        self.next=None

def check_cycle(node):

    try:

        fast = node.next.next
        slow = node.next
    except:
        return False

    # node.next = node.next.next # see if gives any error

    while slow != node and slow!=fast:

        try:
            slow=slow.next
        except:
            return False


        try:
            fast = fast.next.next
        except:
            return False

    return True