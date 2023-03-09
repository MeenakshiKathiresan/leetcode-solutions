# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        cycle = False
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
              
                cycle = True
                break
                
        if cycle:
            if head == slow: return head
            while head != slow:
                head = head.next
                slow = slow.next
                
                if head == slow:
                    return head
            
            
        
        
        return None
        