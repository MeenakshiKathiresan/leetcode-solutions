class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.queue = []
        self.size = k
        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.queue) < self.size:
            self.queue.insert(0, value)
            return True
        return False
        

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.queue) < self.size:
            self.queue.append(value)
            return True
        return False

    def deleteFront(self):
        """
        :rtype: bool
        """
        if len(self.queue) > 0:
            self.queue.pop(0)
            return True
        return False

    def deleteLast(self):
        """
        :rtype: bool
        """
        if len(self.queue) > 0:
            self.queue.pop()
            return True
        return False
        

    def getFront(self):
        """
        :rtype: int
        """
        if len(self.queue) > 0:
            return self.queue[0]
        return -1

    def getRear(self):
        """
        :rtype: int
        """
        if len(self.queue) > 0:
            return self.queue[-1]
        return -1
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return len(self.queue) == self.size


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()