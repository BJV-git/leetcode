# why chosen list also here
#1. all need to be done is that we need to add lists such that we can add elements at the start of teh list so teh overall
# complexity is maintained at O(1)

class dequeue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items ==[]

    def size(self):
        return len(self.items)

    def add_f(self, item):
        self.items.insert(0,item)

    def add_l(self, item):
        self.items.append(item)

    def remove_f(self):
        if not self.isEmpty():

            return self.items.pop(0)
        else:
            return "queue is empty"

    def remove_l(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return "queue is empty"



s= dequeue()
print(s.isEmpty())
s.add_f(3)
s.add_l('Hi')
s.add_f(False)
print(s.size())
print(s.remove_f())
print(s.remove_l())

