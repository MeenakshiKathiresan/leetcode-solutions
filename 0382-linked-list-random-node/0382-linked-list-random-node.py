# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import random
class Solution:
    
    

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.count = 0
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            self.count += 1
            
        self.count *= 2
        
        # odd numbers
        if fast != None:
            self.count += 1
            
        if not self.head.next:
            self.count = 1

    def getRandom(self) -> int:
        
        randint = random.randint(1,self.count)
        start = self.head
        
        if randint == 1: return start.val
        
        count = 1
        while count < randint:
            start = start.next
            count+= 1
        
        
        return start.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()