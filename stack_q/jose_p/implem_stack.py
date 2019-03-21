# why chosen list
#1. because we can handle lists will in built functions and adding and remiving thme is way easier as its the last element

class stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items ==[]

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return "list is empty"

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return "list is empty"


s= stack()
print(s.isEmpty())
s.push(3)
s.push('Hi')
s.push(False)
print(s.size())
