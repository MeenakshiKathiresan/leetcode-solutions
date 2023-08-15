# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if head == None:
            return None
        
        lower_head = lower = ListNode()
        greater_head = greater = ListNode()
        
        while head:
            
            if head.val < x:
                lower.next = head
                lower = lower.next
            else:
                greater.next = head
                greater = greater.next
            
            head = head.next
        
        greater.next = None
        lower.next = greater_head.next
        
        return lower_head.next