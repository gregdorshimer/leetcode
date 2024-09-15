import heapq

class SmallestInfiniteSet(object):

    def __init__(self):
        self.min = 1
        self.is_val_in_heap = {}
        self.val_heap = []

    def popSmallest(self):
        """
        :rtype: int
        """
        if not self.val_heap:
            smallest = self.min
            self.min += 1
        else:
            smallest = heapq.heappop(self.val_heap)
            del self.is_val_in_heap[smallest]
        return smallest

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num >= self.min or self.is_val_in_heap[num]:
            return
        elif num == self.min - 1:
            self.min -= 1
        else:
            heapq.heappush(self.val_heap, num)
            self.is_val_in_heap[num] = True


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)