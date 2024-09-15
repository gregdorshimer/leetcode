from collections import deque

class RecentCounter(object):
    def __init__(self):
        self.pings = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        while self.pings and self.pings[0] < (t - 3000):
            self.pings.popleft()
        self.pings.append(t)
        return len(self.pings)