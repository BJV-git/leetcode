# logic: we will maintain the heap size as k, so that in the min heap the ans will be the first pop,
# the rest of the elements are not needed.

# we can consider if we got an element greater than the min one

import heapq


class KthLargest(object):
    def __init__(self, k, nums):
        self.q = nums
        self.k = k
        self.l = len(self.q)
        heapq.heapify(self.q)

        while len(self.q) > self.k:
            heapq.heappop(self.q)

    def add(self, val):
        if len(self.q) < self.k:
            heapq.heappush(self.q, val)
        elif self.q[0] < val:
            heapq.heappush(self.q, val)
            while len(self.q) > self.k:
                heapq.heappop(self.q)

        return self.q[0]


