class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mini = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.mini is None:
            self.mini = x
        else:
            self.mini = min(self.mini, x)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            a = self.stack.pop()
            if a == self.mini:
                if self.stack:
                    self.mini = min(self.stack)
                else:
                    self.mini = None
            return a

        else:
            return None

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        return self.mini



        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()