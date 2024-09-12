class StockSpanner(object):

    def __init__(self):
        self.stack = []
        self.day = 0

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.day += 1
        last_day = 0
        while self.stack and price >= self.stack[-1][1]:
            popped = self.stack.pop()
            last_day = popped[0]
        if self.stack:
            last_day = self.stack[-1][0]
        else:
            last_day = 0
        self.stack.append((self.day, price))
        return self.day - last_day


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)