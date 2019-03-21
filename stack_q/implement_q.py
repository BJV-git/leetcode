class MyQueue(object):
    def __init__(self):

        self.queue = []
        """
        Initialize your data structure here.
        """

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.queue:
            return self.queue.pop(0)
        else:
            return None

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.queue:
            return self.queue[0]
        else:
            return None

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.queue) == 0




        # Your MyQueue object will be instantiated and called as such:
        # obj = MyQueue()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.peek()
        # param_4 = obj.empty()