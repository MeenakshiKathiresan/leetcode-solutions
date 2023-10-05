# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head

        
        length = 1 
        tail = head  
        while tail.next:
            tail = tail.next
            length += 1

        k %= length

        if k == 0:
            return head

        new_head = head
        for _ in range(length - k - 1):
            new_head = new_head.next

        new_tail = new_head
        new_head = new_head.next
        new_tail.next = None 

        tail.next = head

        return new_head