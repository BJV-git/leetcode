
# logic: basically in queue we gonna maintain the pings so that the difference is still gonna be 3000
# we do maintain the diff and make sure it sum up to 3001 if > will pop till it becomes
# and return the count

import collections

# class RecentCounter(object):
#     def __init__(self):
#         self.q = collections.deque()
#         self.count=0
#     def ping(self, t):
#         self.q.append(t)
#         self.count+=1
#         while self.q[0] < t-3000:
#             self.q.popleft()
#             self.count-=1
#         return self.count

class RecentCounter(object):
    def __init__(self):
        self.queue=[]
        self.count=1
        self.sum = 0
        self.curr=0
        self.flag = 0
    def ping(self, t):
        diff = t - self.curr
        self.queue.append(diff)
        self.count+=1
        self.curr = t
        self.sum+=diff
        if self.flag ==0:
            self.count-=1
            self.flag=1


        if self.sum > 3001:
            while self.sum > 3001:
                pop = self.queue.pop(0)
                self.sum-=pop
                self.count-=1

        return self.count