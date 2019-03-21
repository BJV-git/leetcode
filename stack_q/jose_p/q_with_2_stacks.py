# logic: learned
# first when we encounter the dequeue lets reverse the order into the final list and then keep popping,
# again if the out-stack is empty then we can loop through the in-stack adn again repeat

class stack2Q(object):

    def __init__(self):
        self.instack=[]
        self.outstack=[]

    def enq(self, elem):
        self.instack.append(elem)

    def deq(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()

