# logic: can explode the list in to big one, but waste of extra space
# can calculate the next item by sum and subtraction and validation

class RLEIterator:
    def __init__(self, A):
        self.A = A
        self.lena = len(A)
        self.output=[None]
        self.position =0

    def next(self, n):

        # skip = n
        n=n[0]
        while n >= 0 and self.position < self.lena-1:
            if n - self.A[self.position] <=0:
                self.A[self.position] -= n
                # print(self.A)
                self.output.append(self.A[self.position+1])
                break
            else:
                n = n -  self.A[self.position]
                self.position += 2  # why? = caz we take all the stuff of self.position from n as nothing left more we move out to next
        # print("n", n)
        # print("self.position", self.position)
        # print("A", self.A)

        if self.position > self.lena -2:
            self.output.append(-1)
        print(self.output[-1])
        # print("")

# Your RLEIterator object will be instantiated and called as such:
obj = RLEIterator([3,8,0,9,2,5])
param_1 = obj.next([2])
param_1 = obj.next([1])
param_1 = obj.next([1])
param_1 = obj.next([1])
