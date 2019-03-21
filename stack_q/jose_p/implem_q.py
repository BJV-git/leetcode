# why chosen list also here
#1. all need to be done is that we need to add lists such that we can add elements at the start of teh list so teh overall
# complexity is maintained at O(1)

class queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items ==[]

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return "queue is empty"

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return "list is empty"


s= queue()
print(s.isEmpty())
s.enqueue(3)
s.enqueue('Hi')
s.enqueue(False)
print(s.size())
(s.dequeue())
print(s.dequeue())

