from heapq import heapify, heappush, heappop
class SmallestInfiniteSet(object):

    def __init__(self):
        self.heap = []
        self.present = set()
        self.current = 1

    def popSmallest(self):
        """
        :rtype: int
        """
        if len(self.heap):
            smallest = heappop(self.heap)
            self.present.remove(smallest)
        else:
            smallest = self.current
            self.current += 1
        return smallest

    def addBack(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num < self.current and num not in self.present:
            self.present.add(num)
            heappush(self.heap, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)